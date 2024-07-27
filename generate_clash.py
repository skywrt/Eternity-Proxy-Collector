# generate_clash.py
def generate_clash(nodes):
    clash_config = {
        "proxies": [],
        "proxy-groups": []
    }
    for node in nodes:
        clash_config["proxies"].append({
            "name": node['name'],
            "type": "ss",
            "server": node['server'],
            "port": node['port'],
            "cipher": node['cipher'],
            "password": node['password']
        })
    
    # 这里你可以根据需求添加 proxy-groups

    return clash_config

if __name__ == "__main__":
    nodes = [
        {"name": "Node1", "server": "node1.example.com", "port": 12345, "cipher": "aes-256-gcm", "password": "password1"},
        # 添加更多节点
    ]
    clash_config = generate_clash(nodes)
    print(clash_config)
