import requests
import os
from utils import decode_base64, test_node_availability
from v2ray_config import generate_v2rayn_base64
from clash_config import generate_clash_yaml

V2RAYN_URL = 'https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt'
CLASH_URL = 'https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num'

def fetch_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def main():
    # 创建config目录
    os.makedirs('config', exist_ok=True)
    
    # Fetch base64 encoded node lists
    v2rayn_base64 = fetch_content(V2RAYN_URL)
    clash_base64 = fetch_content(CLASH_URL)

    # Decode the base64 lists
    v2rayn_nodes = decode_base64(v2rayn_base64)
    clash_nodes = decode_base64(clash_base64)

    # Test node availability
    available_v2rayn_nodes = [node for node in v2rayn_nodes if test_node_availability(node)]
    available_clash_nodes = [node for node in clash_nodes if test_node_availability(node)]

    # Generate configuration files
    generate_v2rayn_base64(available_v2rayn_nodes, 'config/v2rayn_nodes_base64.txt')
    generate_clash_yaml(available_clash_nodes, 'config/clash_nodes.yaml')

if __name__ == '__main__':
    main()
