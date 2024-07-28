#!/usr/bin/env python3

import os
import json
import re
import yaml
import subprocess
from urllib import request

sub_list_path = './subs/'
merged_sub_output_file_v2ray = './output/merged_v2ray_sub.txt'
merged_sub_output_file_clash = './output/merged_clash_sub.yaml'

# Function to perform speed test on a server
def speed_test(server_url):
    try:
        result = subprocess.run(['speedtest-cli', '--server', server_url], capture_output=True, text=True)
        speed = re.search(r'Download:\s+([0-9.]+)\s+Mbit/s', result.stdout)
        if speed:
            return float(speed.group(1))
        else:
            return None
    except Exception as e:
        print(f"Speed test failed for {server_url}: {e}")
        return None

class SubConverter:
    def convert_remote(self, url, format_from, format_to):
        try:
            url = f'http://127.0.0.1:25500/sub?target={format_to}&url={url}'
            response = request.urlopen(url)
            return response.read().decode('utf-8')
        except Exception as e:
            return str(e)

    def main(self, content, format_from, format_to, options=None):
        url = f'http://127.0.0.1:25500/sub?target={format_to}'
        data = content.encode('utf-8')
        req = request.Request(url, data=data)
        response = request.urlopen(req)
        return response.read().decode('utf-8')

sub_convert = SubConverter()

class SubMerge:
    def sub_merge(self, url_list):
        content_list_v2ray = []
        content_list_clash = []

        # Clear previous files
        for root, _, files in os.walk(sub_list_path):
            for f in files:
                os.remove(os.path.join(root, f))

        for index, url_container in enumerate(url_list):
            ids = url_container['id']
            remarks = url_container['remarks']
            url = url_container["url"]
            
            # Convert URL to V2ray and Clash formats
            print(f"Converting {remarks} to V2ray and Clash formats...")
            content_v2ray = sub_convert.convert_remote(url, 'url', 'v2ray')
            content_clash = sub_convert.convert_remote(url, 'url', 'clash')

            if content_v2ray and content_clash:
                content_list_v2ray.append(content_v2ray)
                content_list_clash.append(content_clash)
            else:
                print(f"Failed to convert {remarks}")

        # Merge V2ray and Clash contents
        final_content_v2ray = "\n".join(content_list_v2ray)
        final_content_clash = "\n".join(content_list_clash)

        # Write merged content to output files
        with open(merged_sub_output_file_v2ray, 'w', encoding='utf-8') as f:
            f.write(final_content_v2ray)
        
        with open(merged_sub_output_file_clash, 'w', encoding='utf-8') as f:
            f.write(final_content_clash)

        print('Merged V2ray and Clash content written to files.')

        # Speed test for Clash nodes
        clash_nodes = yaml.safe_load(final_content_clash)['proxies']
        speeds = [(node['server'], speed_test(node['server'])) for node in clash_nodes]
        speeds.sort(key=lambda x: x[1], reverse=True)
        
        print("Speed test results:")
        for server, speed in speeds:
            print(f"{server}: {speed} Mbit/s")

if __name__ == '__main__':
    # Load subscription URLs from YAML configuration
    url_list = []
    config_path = './local/server/Subscription.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        try:
            url_list = yaml.safe_load(f.read())
        except yaml.YAMLError as e:
            print("Invalid YAML file.")
            print(e)
            exit(1)

    # Merge and process subscriptions
    sub_merge = SubMerge()
    sub_merge.sub_merge(url_list)
