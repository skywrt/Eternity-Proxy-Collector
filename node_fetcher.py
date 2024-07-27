# node_fetcher.py
import requests

def fetch_nodes(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()  # 假设返回的是 JSON 格式的节点列表
    else:
        print("Failed to fetch nodes")
        return []

if __name__ == "__main__":
    api_url = "https://example.com/api/nodes"  # 替换为实际的节点 API
    nodes = fetch_nodes(api_url)
    print(nodes)
