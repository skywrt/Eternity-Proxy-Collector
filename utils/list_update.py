#!/usr/bin/env python3

from datetime import datetime
import json
import requests
from requests.adapters import HTTPAdapter

# 文件路径定义
sub_list_json = './sub/sub_list.json'

def url_updated(url):  # 判断远程远程链接是否已经更新
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    try:
        resp = s.get(url, timeout=4)
        status = resp.status_code
    except Exception:
        status = 404
    return status == 200

class update_url():
    def update_main(use_airport=False, airports_id=None, sub_list_json='./sub/sub_list.json'):
        if airports_id is None:
            airports_id = [5]
        
        with open(sub_list_json, 'r', encoding='utf-8') as f:  # 载入订阅链接
            raw_list = json.load(f)
        
        for sub in raw_list:
            id = sub['id']
            current_url = sub['url']
            if not use_airport:
                if id not in airports_id and sub['update_method'] != 'update_airports':
                    try:
                        if sub['update_method'] != 'auto' and sub['enabled']:
                            print(f'Finding available update for ID{id}')
                            if sub['update_method'] == 'change_date':
                                new_url = update_url.change_date(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                            elif sub['update_method'] == 'page_release':
                                new_url = update_url.find_link(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                            elif sub['update_method'] == 'update_airports':
                                new_url = update_url.update_airports(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                    except KeyError:
                        print(f'{id} Url not changed! Please define update method.')

            else:
                if id in airports_id:
                    try:
                        if sub['update_method'] != 'auto' and sub['enabled']:
                            print(f'Finding available update for ID{id}')
                            if sub['update_method'] == 'change_date':
                                new_url = update_url.change_date(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                            elif sub['update_method'] == 'page_release':
                                new_url = update_url.find_link(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                            elif sub['update_method'] == 'update_airports':
                                new_url = update_url.update_airports(id, current_url)
                                if new_url == current_url:
                                    print(f'No available update for ID{id}\n')
                                else:
                                    sub['url'] = new_url
                                    print(f'ID{id} url updated to {new_url}\n')
                    except KeyError:
                        print(f'{id} Url not changed! Please define update method.')

        updated_list = json.dumps(raw_list, sort_keys=False, indent=2, ensure_ascii=False)
        with open(sub_list_json, 'w', encoding='utf-8') as file:
            file.write(updated_list)

    def update_airports(id, current_url):
        if id == 5:
            s = requests.Session()
            s.mount('http://', HTTPAdapter(max_retries=2))
            s.mount('https://', HTTPAdapter(max_retries=2))
            urllist = list(set(filter(lambda x: x and x.startswith("http"), s.get(
                'https://raw.githubusercontent.com/RenaLio/Mux2sub/main/urllist', timeout=4).text.split("\n"))))
            sublist = list(set(filter(lambda x: x and x.startswith("http"), s.get(
                'https://raw.githubusercontent.com/RenaLio/Mux2sub/main/sub_list', timeout=4).text.split("\n"))))
            air_free = list(set(filter(lambda x: x and x.startswith("http"), s.get(
                'https://raw.githubusercontent.com/rxsweet/getAirport/main/config/sublist_free', timeout=4).text.split("\n"))))
            air_mining = list(set(filter(lambda x: x and x.startswith("http"), s.get(
                'https://raw.githubusercontent.com/rxsweet/getAirport/main/config/sublist_mining', timeout=4).text.split("\n"))))

            urllist.extend(sublist)
            urllist.extend(air_free)
            urllist.extend(air_mining)

            new_url = "|".join(list(set(urllist)))
        return new_url

    def change_date(id, current_url):
        if id == 0:
            today = datetime.today().strftime('%m%d')
            url_front = 'https://raw.githubusercontent.com/pojiezhiyuanjun/freev2/master/'
            url_end = '.txt'
            new_url = url_front + today + url_end
        elif id == 1:
            today = datetime.today().strftime('%Y%m%d')
            this_year = datetime.today().strftime('%Y')
            this_month = datetime.today().strftime('%m')
            url_front = 'https://nodefree.org/dy/'
            url_end = '.yaml'
            new_url = url_front + this_year + '/' + this_month + '/' + today + url_end
        elif id == 3:
            today = datetime.today().strftime('%Y%m%d')
            this_month = datetime.today().strftime('%m')
            this_year = datetime.today().strftime('%Y')
            url_front = 'https://v2rayshare.com/wp-content/uploads/'
            url_end = '.txt'
            new_url = url_front + "/".join([this_year, this_month, today]) + url_end
        elif id == 4:
            today = datetime.today().strftime('%Y%m%d')
            this_month = datetime.today().strftime('%m')
            this_year = datetime.today().strftime('%Y')
            url_front = 'https://clashnode.com/wp-content/uploads/'
            url_end = '.txt'
            new_url = url_front + "/".join([this_year, this_month, today]) + url_end

        if url_updated(new_url):
            return new_url
        else:
            return current_url

    def find_link(id, current_url):
        if id == 2:
            try:
                res_json = requests.get(
                    'https://api.github.com/repos/mianfeifq/share/contents/').json()
                for file in res_json:
                    if file['name'].startswith('data'):
                        return file['download_url']
                else:
                    return current_url
            except Exception:
                return current_url

if __name__ == '__main__':
    update_url.update_main()
