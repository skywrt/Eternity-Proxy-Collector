# V2ray-Clash-Node-Checker

这个项目用于从指定的Base64编码节点链接中提取节点，进行测速分析，剔除不可用的节点，并生成适用于v2rayN和Clash代理软件的配置文件。

## 使用方法

1. 克隆项目：
    ```
    git clone https://github.com/your-username/V2ray-Clash-Node-Checker.git
    ```

2. 安装依赖：
    ```
    pip install -r requirements.txt
    ```

3. 运行主脚本：
    ```
    python main.py
    ```

4. 生成的配置文件将会保存在`config`目录下。

## GitHub Actions

该项目已配置GitHub Actions工作流，每次代码推送或每天定期执行，将自动进行节点的测速和配置文件的生成。
