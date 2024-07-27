import base64
import subprocess
import json

def decode_base64(data):
    decoded_bytes = base64.b64decode(data.strip())
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str.splitlines()

def test_node_availability(node):
    try:
        config = create_xray_config(node)
        with open('test_config.json', 'w') as f:
            json.dump(config, f)
        
        # 使用xray来测试节点连通性
        result = subprocess.run(['xray', 'run', '-c', 'test_config.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        print(f"Testing node {node}, return code: {result.returncode}")  # 添加调试输出
        return result.returncode == 0
    except Exception as e:
        print(f"Error testing node {node}: {e}")
        return False

def create_xray_config(node):
    # 这里应添加解析节点并生成适用于xray的配置逻辑
    # 目前只是一个示例，需根据实际情况修改
    return {
        "log": {
            "loglevel": "warning"
        },
        "inbounds": [],
        "outbounds": [
            {
                "protocol": "freedom",
                "settings": {},
                "tag": "direct"
            },
            {
                "protocol": "blackhole",
                "settings": {},
                "tag": "blocked"
            },
            {
                "protocol": "vmess",
                "settings": {
                    "vnext": [
                        {
                            "address": "example.com",
                            "port": 443,
                            "users": [
                                {
                                    "id": "your-uuid-here",
                                    "alterId": 64,
                                    "security": "auto"
                                }
                            ]
                        }
                    ]
                },
                "tag": "proxy"
            }
        ],
        "routing": {
            "domainStrategy": "IPOnDemand",
            "rules": [
                {
                    "type": "field",
                    "outboundTag": "proxy",
                    "domain": [
                        "geosite:google"
                    ]
                }
            ]
        }
    }
