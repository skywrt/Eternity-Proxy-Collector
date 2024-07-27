IndentationError 通常是由于 Python 代码中的缩进不一致引起的。在 Python 中，缩进是语法的一部分，因此每个代码块（如函数、循环、条件语句等）都必须正确缩进。

在你提供的错误信息中，generate_clash.py 的第 22 行出现了缩进错误。请确保在 generate_clash.py 中的所有代码块都有正确的缩进。以下是修正后的 generate_clash.py 脚本示例，确保所有代码行都正确缩进：

修正后的 generate_clash.py
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
        # 这里解析每个节点的配置并添加到 clash_config 中
        # 假设每行是一个节点的配置
        # 需要根据实际配置格式进行解析
        # 例如，假设 config 是 JSON 格式的节点
        # 你需要将其解析为字典并添加到 clash_config 中

        # 示例解析（根据实际格式进行调整）
        # node = json.loads(config)
        # clash_config['outbounds'][0]['settings']['vnext'].append(node)

    with open('clash_config.yaml', 'w') as f:
        f.write(str(clash_config))  # 根据实际格式保存为 YAML

if __name__ == "__main__":
    generate_clash_config()
