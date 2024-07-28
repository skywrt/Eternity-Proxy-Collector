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

# 生成v2ray和clash配置文件
echo "生成配置文件..."
python <<EOF
import base64

def decode_base64(encoded):
    try:
        return base64.urlsafe_b64decode(encoded + '=' * (-len(encoded) % 4)).decode('utf-8')
    except Exception as e:
        return str(e)

with open('v2ray_base64.txt', 'r') as f:
    v2ray_base64 = f.read().strip()
with open('clash_base64.txt', 'r') as f:
    clash_base64 = f.read().strip()

v2ray_decoded = decode_base64(v2ray_base64)
clash_decoded = decode_base64(clash_base64)

with open('v2ray.txt', 'w') as f:
    f.write(v2ray_decoded)
with open('clash.yaml', 'w') as f:
    f.write(clash_decoded)

print("v2ray和clash配置文件生成成功")
EOF

echo "获取订阅成功"
echo "希望你有美好的一天~"
echo "再见~"
