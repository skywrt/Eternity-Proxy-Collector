import base64

def decode_base64(data):
    decoded_bytes = base64.b64decode(data)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str.splitlines()

def test_node_availability(node):
    # 这里应添加实际的节点测速逻辑
    # 目前只是一个示例，假设所有节点都可用
    return True
