import base64

def generate_v2rayn_base64(nodes, output_file):
    if not nodes:
        print("No V2rayN nodes to encode.")  # 添加调试输出
    encoded_nodes = [base64.b64encode(node.encode('utf-8')).decode('utf-8') for node in nodes]
    with open(output_file, 'w') as f:
        f.write('\n'.join(encoded_nodes))
