import base64

def generate_v2rayn_base64(nodes, output_file):
    encoded_nodes = [base64.b64encode(node.encode('utf-8')).decode('utf-8') for node in nodes]
    with open(output_file, 'w') as f:
        f.write('\n'.join(encoded_nodes))
