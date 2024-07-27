import json

def parse_v2ray_config(config_str: str) -> dict:
    try:
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        log(f'解析 V2Ray 配置失败: {e}')
        return {}

def generate_v2ray_config(proxies: list) -> str:
    try:
        config = {
            'outbounds': [
                {
                    'protocol': 'vmess',
                    'settings': {
                        'vnext': proxies
                    }
                }
            ]
        }
        return json.dumps(config, indent=2)
    except Exception as e:
        log(f'生成 V2Ray 配置出错: {e}')
        return ''
