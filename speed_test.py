# speed_test.py
import subprocess
import time

def test_node_speed(node):
    start_time = time.time()
    # 这里假设 node 是一个可以用来 ping 的地址
    subprocess.run(["ping", "-c", "4", node])  # 在 Linux/Mac 上
    # subprocess.run(["ping", "-n", "4", node])  # 在 Windows 上
    elapsed_time = time.time() - start_time
    return elapsed_time

if __name__ == "__main__":
    nodes = ["node1.example.com", "node2.example.com"]  # 替换为实际的节点
    for node in nodes:
        speed = test_node_speed(node)
        print(f"Node: {node}, Speed: {speed} seconds")
