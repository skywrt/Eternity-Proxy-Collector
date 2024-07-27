import yaml

def generate_clash_config(proxies: list, rules: list) -> str:
    try:
        config = {
            'proxies': proxies,
            'proxy-groups': [
                {
                    'name': 'Proxy',
                    'type': 'select',
                    'proxies': [proxy['name'] for proxy in proxies]
                }
            ],
            'rules': rules
        }
        # 使用安全的 YAML 库函数生成配置
        return yaml.dump(config, allow_unicode=True, sort_keys=False)
    except Exception as e:
        log(f'生成 Clash 配置出错: {e}')
        return ''

def save_clash_config(config_str: str, file_path: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(config_str)
    except Exception as e:
        log(f'保存 Clash 配置文件出错: {e}')
