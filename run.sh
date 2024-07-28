import base64
import requests
import speedtest
import json
import yaml

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

try:
    v2ray_nodes = json.loads(v2ray_decoded)
except json.JSONDecodeError as e:
    print(f"Error decoding v2ray base64 content: {e}")
    v2ray_nodes = []

try:
    clash_nodes = yaml.safe_load(clash_decoded)
except yaml.YAMLError as e:
    print(f"Error decoding clash base64 content: {e}")
    clash_nodes = {'proxies': []}

valid_v2ray_nodes = []
valid_clash_nodes = []

for node in v2ray_nodes:
    if check_node_connectivity('https://www.google.com'):
        speed = get_node_speed()
        if speed > 1:  # 设定一个最小的可接受速度，比如 1 Mbps
            valid_v2ray_nodes.append(node)

for node in clash_nodes.get('proxies', []):
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
