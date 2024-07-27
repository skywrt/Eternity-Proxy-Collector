import base64 as pybase64
import binascii

def decode_base64(encoded):
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            # Padding with '=' to make the length of encoded string a multiple of 4
            padded_encoded = encoded + '=' * (-len(encoded) % 4)
            # Decode the Base64 encoded string
            decoded = pybase64.b64decode(padded_encoded).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error) as e:
            print(f"Decoding error with encoding {encoding}: {e}")
            continue
    return decoded

def test_node_availability(node):
    try:
        config = create_xray_config(node)
        with open('test_config.json', 'w') as f:
            json.dump(config, f)
        
        result = subprocess.run(['xray', 'run', '-c', 'test_config.json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        print(f"Testing node {node}, return code: {result.returncode}, stderr: {result.stderr.decode()}")  # 打印错误信息
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
