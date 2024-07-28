#!/usr/bin/env python3

from sub_convert import sub_convert
from list_update import update_url
from get_subs import subs
import json
import re
import os
import yaml
from urllib import request

# 文件路径定义
Eterniy = './Eternity'
readme = './README.md'
sub_list_json = './sub/sub_list.json'
sub_merge_path = './sub/'
sub_list_path = './sub/list/'

ipv4 = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
ipv6 = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'

def add_valid(line):
    if (line.__contains__("ssr://") or line.__contains__("ss://")
            or line.__contains__("trojan://") or line.__contains__("vmess://")):
        return line
    return ''

class sub_merge():
    def sub_merge(url_list):  # 将转换后的所有 Url 链接内容合并转换 YAML or Base64, ，并输出文件，输入订阅列表。
        content_list = []
        for t in os.walk(sub_list_path):
            for f in t[2]:
                f = t[0] + f
                os.remove(f)

        for (index, url_container) in enumerate(url_list):
            ids = url_list[index]['id']
            remarks = url_list[index]['remarks']
            if type(url_container['url']) == list:
                for each_url in url_container["url"]:
                    content = ''
                    print("gather server from " + each_url)
                    content += sub_convert.convert_remote(
                        each_url, 'url', 'http://127.0.0.1:25500')

                    if content == 'Url 解析错误':
                        content = sub_convert.main(each_url, 'url', 'url')
                        if content != 'Url 解析错误':
                            if add_valid(content) != '':
                                content_list.append(content)
                            else:
                                print(f'this url failed {each_url}')
                            print(
                                f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                        else:
                            print(
                                f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write(content)
                        file.close()
                    elif content == 'Url 订阅内容无法解析':
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write('Url Subscription could not be parsed')
                        file.close()
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                    elif content != None:
                        if add_valid(content) != '':
                            content_list.append(content)
                        else:
                            print(f'this url failed {each_url}')
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write(content)
                        file.close()
                        print(
                            f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                    else:
                        file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                    'a+', encoding='utf-8')
                        file.write('Url Subscription could not be parsed')
                        file.close()
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')

            else:
                each_url = url_container["url"]
                content = ''
                print("gather server from " + each_url)
                content += sub_convert.convert_remote(
                    each_url, 'url', 'http://127.0.0.1:25500')

                if content == 'Url 解析错误':
                    content = sub_convert.main(each_url, 'url', 'url')
                    if content != 'Url 解析错误':
                        if add_valid(content) != '':
                            content_list.append(content)
                        else:
                            print(f'this url failed {each_url}')

                        print(
                            f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                    else:
                        print(
                            f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write(content)
                    file.close()
                elif content == 'Url 订阅内容无法解析':
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write('Url Subscription could not be parsed')
                    file.close()
                    print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')
                elif content != None:
                    content_list.append(content)
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write(content)
                    file.close()
                    print(f'Writing content of {remarks} to {ids:0>2d}.txt\n')
                else:
                    file = open(f'{sub_list_path}{ids:0>2d}.txt',
                                'a+', encoding='utf-8')
                    file.write('Url Subscription could not be parsed')
                    file.close()
                    print(f'Writing error of {remarks} to {ids:0>2d}.txt\n')

            print('already gathered ' +
                  str(''.join(content_list).split('\n').__len__()))
            print('\n')

        print('Merging nodes...\n')
        content_list = list(
            filter(lambda x: x != '', ''.join(content_list).split("\n")))
        content_list = list(filter(lambda x: x.startswith("ssr://") or x.startswith("ss://")
                                   or x.startswith("trojan://") or x.startswith("vmess://"), content_list))
        content_list = list(
            filter(lambda x: x.__contains__("订阅内容解析错误") == False, content_list))
        content_raw = "\n".join(content_list)

        print(f"it's fine till here with {content_list.__len__()} lines")

        content_yaml = sub_convert.main(content_raw, 'content', 'YAML', {
            'dup_rm_enabled': True, 'format_name_enabled': True})

        yaml_proxies = content_yaml.split('\n')[1:]
        temp = list(filter(lambda x: re.search(ipv6, x) == None, yaml_proxies))
        temp = list(filter(lambda x: re.search(ipv4, x) == None, yaml_proxies))

        temp = yaml.safe_load("\n".join(temp))
        print(temp)
        if temp.__contains__("proxies"):
            yaml_proxies = temp['proxies']
        else:
            yaml_proxies = temp

        content_raw = sub_convert.main(content_raw, 'content', 'url')
        content_raw = sub_convert.main(content_raw, 'content', 'Base64')
        print("Converting to Base64")

        file = open(f'{sub_merge_path}node.txt', 'w+', encoding='utf-8')
        file.write(content_raw)
        file.close()

        file = open(f'{sub_merge_path}node.yaml', 'w+', encoding='utf-8')
        yaml.dump({'proxies': yaml_proxies}, file)
        file.close()
        return {'yaml': yaml_proxies, 'base64': content_raw}


def readme_update(readme, sub_list_json):
    try:
        with open(sub_list_json, 'r', encoding='utf-8') as f:
            sub_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: {sub_list_json} not found")
        return

    headers = [
        "| Index | Provider | Subscriptions |",
        "|:-----:|:---------:|:-------------:|"
    ]

    table_rows = []
    for idx, sub in enumerate(sub_list, 1):
        provider = sub.get("remarks", "")
        urls = sub.get("url", [])
        if isinstance(urls, list):
            urls = ", ".join(urls)
        table_rows.append(f"| {idx} | {provider} | {urls} |")

    table = "\n".join(headers + table_rows)

    readme_lines = []
    try:
        with open(readme, 'r', encoding='utf-8') as f:
            readme_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {readme} not found")
        return

    table_start_idx = -1
    table_end_idx = -1

    for i, line in enumerate(readme_lines):
        if line.strip() == headers[0]:
            table_start_idx = i
        if table_start_idx != -1 and line.strip() == "":
            table_end_idx = i
            break

    if table_start_idx != -1 and table_end_idx != -1:
        readme_lines = (
            readme_lines[:table_start_idx]
            + headers + table_rows
            + readme_lines[table_end_idx:]
        )
    else:
        readme_lines.extend(headers + table_rows)

    with open(readme, 'w', encoding='utf-8') as f:
        f.writelines(readme_lines)


if __name__ == "__main__":
    # Load the subscription list JSON
    try:
        with open(sub_list_json, 'r', encoding='utf-8') as f:
            sub_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: {sub_list_json} not found")
        sub_list = []

    # Update URLs
    updated_sub_list = update_url(sub_list)

    # Merge subscriptions
    merged_subs = sub_merge.sub_merge(updated_sub_list)

    # Update README
    readme_update(readme, sub_list_json)

    # Save updated subscription list
    with open(sub_list_json, 'w', encoding='utf-8') as f:
        json.dump(updated_sub_list, f, ensure_ascii=False, indent=4)
