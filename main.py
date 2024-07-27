import argparse
import requests
import base64
import yaml
import json
from v2ray_config import decode_base64, generate_v2ray_configs
from clash_config import generate_clash_configs
from utils import log, save_to_file, test_proxies

def download_file(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as f:
        f.write(response.content)
    log(f"Downloaded {file_path}")

def main(config_path, output_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    v2ray_base64_url = config.get('v2ray_base64_url')
    clash_base64_url = config.get('clash_base64_url')

    if not v2ray_base64_url or not clash_base64_url:
        raise ValueError("Both v2ray_base64_url and clash_base64_url must be provided in the config.")

    # Download base64 encoded configurations
    download_file(v2ray_base64_url, 'v2ray_base64.txt')
    download_file(clash_base64_url, 'clash_base64.txt')

    # Decode base64 encoded nodes
    with open('v2ray_base64.txt', 'r') as file:
        v2ray_base64_nodes = file.read().splitlines()
    
    with open('clash_base64.txt', 'r') as file:
        clash_base64_nodes = file.read().splitlines()

    v2ray_nodes = [decode_base64(node) for node in v2ray_base64_nodes]
    clash_nodes = [decode_base64(node) for node in clash_base64_nodes]

    # Test proxies
    valid_v2ray_nodes = test_proxies(v2ray_nodes)
    valid_clash_nodes = test_proxies(clash_nodes)

    # Generate configurations
    v2ray_configs = generate_v2ray_configs(valid_v2ray_nodes)
    clash_configs = generate_clash_configs(valid_clash_nodes)

    # Save results
    save_to_file('v2rayn_nodes_base64.txt', base64.b64encode('\n'.join(v2ray_configs).encode('utf-8')))
    with open(output_path, 'w') as f:
        yaml.dump(clash_configs, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process configuration files and generate node configurations.")
    parser.add_argument('config_path', help="Path to the YAML configuration file")
    parser.add_argument('output_path', help="Path to save the generated Clash configuration file")
    args = parser.parse_args()
    main(args.config_path, args.output_path)
