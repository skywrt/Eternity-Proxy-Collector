#!/bin/bash

currentdate=$(date +%Y%m%d)  
currentmonth=$(date +%Y%m)
currentmonths=$(date +%m)
currentyears=$(date +%Y)

# 替换为你的 base64 编码节点链接
subscribeclash="https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt"
subscribeV2ray="https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num"

# 如果文件存在，删除旧的配置文件
if [ -f "./clash.yaml" ]; then
  rm ./clash.yaml
fi

if [ -f "./v2ray.txt" ]; then
  rm ./v2ray.txt
fi

# 下载订阅内容
echo "获取订阅..."
wget $subscribeclash -O ./clash_base64.txt
wget $subscribeV2ray -O ./v2ray_base64.txt

# 安装 Python 依赖
pip install requests speedtest-cli

# 生成v2ray和clash配置文件
echo "生成配置文件并检查节点..."
python <<EOF
import base64
import requests
import speedtest
import json

def decode_base64(encoded):
    try:
        return base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4)).decode('utf-8')
    except Exception as e:
        return str(e)

def check_node_connectivity(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def get_node_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        return st.results.download / 1e6  # 返回 Mbps
    except:
        return 0

with open('v2ray_base64.txt', 'r') as f:
    v2ray_base64 = f.read().strip()
with open('clash_base64.txt', 'r') as f:
    clash_base64 = f.read().strip()

v2ray_decoded = decode_base64(v2ray_base64)
clash_decoded = decode_base64(clash_base64)

v2ray_nodes = json.loads(v2ray_decoded)
clash_nodes = yaml.safe_load(clash_decoded)

valid_v2ray_nodes = []
valid_clash_nodes = []

for node in v2ray_nodes:
    if check_node_connectivity('https://www.google.com'):
        speed = get_node_speed()
        if speed > 1:  # 设定一个最小的可接受速度，比如 1 Mbps
            valid_v2ray_nodes.append(node)

for node in clash_nodes['proxies']:
    if check_node_connectivity('https://www.google.com'):
        speed = get_node_speed()
        if speed > 1:  # 设定一个最小的可接受速度，比如 1 Mbps
            valid_clash_nodes.append(node)

with open('v2ray.txt', 'w') as f:
    f.write(base64.urlsafe_b64encode(json.dumps(valid_v2ray_nodes).encode()).decode('utf-8'))
with open('clash.yaml', 'w') as f:
    clash_nodes['proxies'] = valid_clash_nodes
    yaml.safe_dump(clash_nodes, f, default_flow_style=False)

print("v2ray和clash配置文件生成成功")
EOF

echo "获取订阅成功"
echo "希望你有美好的一天~"
echo "再见~"
