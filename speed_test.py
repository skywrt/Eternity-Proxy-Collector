import subprocess

def speed_test():
    # 假设使用某个命令行工具进行节点速度测试
    # 这里可以使用实际的速度测试代码
    result = subprocess.run(['ping', 'example.com'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    speed_test()
