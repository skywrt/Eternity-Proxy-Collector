
import os
import base64

def sort_nodes(input_file, output_folder):
    # 实现节点分类逻辑
    pass  # 这里可以实现具体的分类逻辑

def main():
    input_file = 'output.yaml'  # 之前生成的文件
    output_folder = 'SortedNodes'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    sort_nodes(input_file, output_folder)

if __name__ == "__main__":
    main()
