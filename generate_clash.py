import yaml

def generate_clash_config():
    with open('decoded_configs.txt', 'r') as f:
        configs = f.readlines()

    clash_config = {
        "outbounds": [
            {
                "tag": "proxy",
                "protocol": "vmess",
                "settings": {
                    "vnext": []
                }
            }
        ]
    }

    for config in configs:
        # Assuming each line is a JSON formatted node
        # You need to parse the config line and append it to the clash_config
        # Example parsing (adjust according to actual format)
        # node = json.loads(config.strip())
        # clash_config['outbounds'][0]['settings']['vnext'].append(node)

        # Ensure you add the parsed node to the clash_config here
        # Example:
        # if node:  # Check if node is valid
        #     clash_config['outbounds'][0]['settings']['vnext'].append(node)

    # Make sure this line is indented correctly
    with open('clash_config.yaml', 'w') as f:
        yaml.dump(clash_config, f)

if __name__ == "__main__":
    generate_clash_config()
