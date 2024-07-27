import requests
import os
from utils import decode_base64, test_node_availability
from v2ray_config import generate_v2rayn_base64
from clash_config import generate_clash_yaml

V2RAYN_URL = 'https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt'
CLASH_URL = 'https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num'

def fetch_content(url):
    print(f"Fetching content from {url}...")  # 添加打印输出
    response = requests.get(url)
    response.raise_for_status()
    print(f"Successfully fetched content from {url}")  # 添加打印输出
    return response.text

def main():
    print("Starting the script...")  # 添加打印输出
    
    # 创建config目录
    os.makedirs('config', exist_ok=True)
    print("Created 'config' directory if it didn't exist.")  # 添加打印输出
    
    # Fetch base64 encoded node lists
    print("Fetching V2rayN base64 nodes...")
    v2rayn_base64 = fetch_content(V2RAYN_URL)
    
    print("Fetching Clash base64 nodes...")
    clash_base64 = fetch_content(CLASH_URL)

    # Decode the base64 lists
    print("Decoding V2rayN base64 nodes...")
    v2rayn_nodes = decode_base64(v2rayn_base64)
    print(f"Decoded {len(v2rayn_nodes)} V2rayN nodes.")  # 打印解码节点的数量
    
    print("Decoding Clash base64 nodes...")
    clash_nodes = decode_base64(clash_base64)
    print(f"Decoded {len(clash_nodes)} Clash nodes.")  # 打印解码节点的数量

    # Test node availability
    print("Testing availability of V2rayN nodes...")
    available_v2rayn_nodes = [node for node in v2rayn_nodes if test_node_availability(node)]
    print(f"Available V2rayN nodes: {len(available_v2rayn_nodes)}")  # 打印可用节点的数量
    
    print("Testing availability of Clash nodes...")
    available_clash_nodes = [node for node in clash_nodes if test_node_availability(node)]
    print(f"Available Clash nodes: {len(available_clash_nodes)}")  # 打印可用节点的数量

    # Generate configuration files
    print("Generating V2rayN configuration file...")
    generate_v2rayn_base64(available_v2rayn_nodes, 'config/v2rayn_nodes_base64.txt')
    print("V2rayN configuration file generated.")
    
    print("Generating Clash configuration file...")
    generate_clash_yaml(available_clash_nodes, 'config/clash_nodes.yaml')
    print("Clash configuration file generated.")

    print("Script completed successfully.")  # 添加打印输出

if __name__ == '__main__':
    main()
