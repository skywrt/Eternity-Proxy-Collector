import base64
import json

def decode_base64(encoded):
    decoded = ''
    for encoding in ['utf-8', 'iso-8859-1']:
        try:
            decoded = base64.urlsafe_b64decode(encoded + b'=' * (-len(encoded) % 4)).decode(encoding)
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
