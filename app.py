import pybase64
import requests
import os
import yaml

def decode_base64(encoded):
    try:
        decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode('utf-8')
        return decoded
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return None

def check_node_availability(node):
    # 这里可以实现节点可用性检查
    # 例如使用 requests.get() 测试节点
    return True  # 假设所有节点都可用，实际情况需要实现检查逻辑

def generate_clash_config(decoded_data):
    clash_config = {
        "outbounds": []
    }

    for node in decoded_data:
        if check_node_availability(node):
            clash_config['outbounds'].append({
                "protocol": "vmess",  # 根据节点类型调整
                "settings": {
                    "vnext": [{
                        "address": "example.com",  # 从节点中解析
                        "port": 10086,  # 从节点中解析
                        "users": [{
                            "id": "uuid",  # 从节点中解析
                            "alterId": 64
                        }]
                    }]
                }
            })

    return clash_config

def main():
    links = [
        'https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt',
        'https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num'
    ]

    decoded_data = []

    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            encoded_links = response.text.splitlines()
            for encoded in encoded_links:
                decoded = decode_base64(encoded)
                if decoded:
                    decoded_data.append(decoded)

    clash_config = generate_clash_config(decoded_data)

    # Save to output.yaml
    with open('output.yaml', 'w') as f:
        yaml.dump(clash_config, f)

if __name__ == "__main__":
    main()
