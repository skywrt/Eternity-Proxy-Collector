import base64

def generate_v2rayn_base64(nodes, output_file):
    if not nodes:
        print("No V2rayN nodes to encode.")
    encoded_nodes = [base64.b64encode(node.encode('utf-8')).decode('utf-8') for node in nodes]
    with open(output_file, 'w') as f:
        f.write('\n'.join(encoded_nodes))
    print(f"Generated V2rayN base64 file with {len(encoded_nodes)} entries.")
