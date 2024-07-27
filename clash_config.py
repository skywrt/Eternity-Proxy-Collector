import yaml

def generate_clash_yaml(nodes, output_file):
    clash_config = {
        'proxies': []
    }

    for node in nodes:
        clash_config['proxies'].append({
            'name': node,  # Adjust according to the actual structure of the node data
            'type': 'vmess',
            'server': node,
            # Add other required fields here
        })

    with open(output_file, 'w') as f:
        yaml.dump(clash_config, f, default_flow_style=False)
