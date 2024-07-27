import base64
import json
import binascii  # 添加导入

def decode_base64(encoded):
    decoded = ''
    encoded_bytes = encoded.encode('utf-8')  # 将字符串转换为字节类型
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = base64.urlsafe_b64decode(encoded_bytes + b'=' * (-len(encoded_bytes) % 4)).decode(encoding)
            break
        except (UnicodeDecodeError, binascii.Error):
            pass
    return decoded

def generate_v2ray_configs(decoded_data):
    configs = []

    for config in decoded_data:
        configs.append(config)

    sorted_configs = sorted(configs)

    return sorted_configs
