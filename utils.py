import base64
import requests

def decode_base64(data):
    decoded_bytes = base64.b64decode(data)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str.splitlines()

def test_node_availability(node):
    try:
        # 测试节点速度
        speed_test_response = requests.get('https://speed.cloudflare.com', proxies={'http': node, 'https': node}, timeout=5)
        speed_test_success = speed_test_response.status_code == 200

        # 测试节点连通性
        connectivity_test_response = requests.get('https://www.google.com/generate_204', proxies={'http': node, 'https': node}, timeout=5)
        connectivity_test_success = connectivity_test_response.status_code == 204

        return speed_test_success and connectivity_test_success
    except Exception as e:
        print(f"Error testing node {node}: {e}")
        return False
