import base64

def generate_v2rayn_base64(nodes, output_file):
    with open(output_file, 'w') as f:
        for node in nodes:
            encoded_node = base64.b64encode(node.encode('utf-8')).decode('utf-8')
            f.write(encoded_node + '\n')
