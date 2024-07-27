import base64
import pybase64

def decode_base64(encoded):
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = pybase64.b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

def generate_v2ray_configs(decoded_data):
    # 直接对解码后的数据进行排序并返回
    sorted_configs = sorted(decoded_data)
    return sorted_configs

def generate_v2rayn_base64(nodes, output_file):
    # 生成 base64 编码的 V2Ray 配置
    encoded_nodes = [base64.b64encode(node.encode('utf-8')).decode('utf-8') for node in nodes]
    with open(output_file, 'w') as f:
        f.write('\n'.join(encoded_nodes))

def parse_v2ray_node(node):
    # 解析 V2Ray 节点信息（这里仅为示例，需根据实际情况修改）
    return {
        'address': 'example.com',
        'port': 443,
        'id': 'your-uuid-here',
        'alterId': 64,
        'security': 'auto'
    }

def create_v2ray_config(node):
    config = parse_v2ray_node(node)
    return {
        "log": {
            "loglevel": "warning"
        },
        "inbounds": [],
        "outbounds": [
            {
                "protocol": "vmess",
                "settings": {
                    "vnext": [
                        {
                            "address": config['address'],
                            "port": config['port'],
                            "users": [
                                {
                                    "id": config['id'],
                                    "alterId": config['alterId'],
                                    "security": config['security']
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
