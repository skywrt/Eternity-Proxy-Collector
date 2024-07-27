import argparse
from v2ray_config import generate_v2ray_config, parse_v2ray_config
from clash_config import generate_clash_config, save_clash_config
from utils import log

def main(config_path: str, output_path: str) -> None:
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config_str = file.read()

        proxies = parse_v2ray_config(config_str).get('outbounds', [{}])[0].get('settings', {}).get('vnext', [])
        clash_config = generate_clash_config(proxies, [])
        save_clash_config(clash_config, output_path)
        log('配置转换成功！')
    except Exception as e:
        log(f'主程序出错: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='转换 V2Ray 配置为 Clash 配置')
    parser.add_argument('config_path', type=str, help='V2Ray 配置文件路径')
    parser.add_argument('output_path', type=str, help='Clash 配置输出文件路径')
    args = parser.parse_args()

    main(args.config_path, args.output_path)
