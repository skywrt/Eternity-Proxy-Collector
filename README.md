# Eternity Proxy Collector

本项目用于收集、合并和测试代理订阅链接，并生成相应的配置文件。通过自动化脚本和 GitHub Actions 工作流，确保代理列表的实时更新和可用性检测。

## 项目简介

Eternity Proxy Collector 是一个自动化工具，旨在帮助用户管理和优化代理订阅链接。主要功能包括：
- 从多个订阅链接收集代理信息
- 合并和转换代理链接为 YAML 和 Base64 格式
- 测试代理节点的速度和可用性
- 更新 README 文件以反映最新的节点信息

# 文件说明

## 脚本文件

- **list_merge.py**：主脚本，用于收集、合并和测试代理订阅链接。
- **sub_convert.py**：用于转换代理链接格式的脚本。
- **update_url.py**：用于更新订阅链接的脚本。
- **get_subs.py**：用于获取代理订阅链接的脚本。
- **test_proxies.py**：用于测试代理节点速度和可用性的脚本。

## 工具文件

- **utils/localserver**：本地服务器相关代码。

## 配置文件

- **sub/sub_list.json**：包含所有订阅链接的 JSON 文件。
- **sub/sub_merge.txt**：合并后的代理链接文本文件。
- **sub/sub_merge_base64.txt**：合并后的 Base64 编码代理链接文件。
- **sub/sub_merge_yaml.yml**：合并后的 YAML 格式代理链接文件。

# 节点信息

## 高速节点
- **high-speed node**: 0

## 所有节点
- **merge nodes w/o dup**: 0

## 节点来源
- **示例节点来源**: 0

# 更新日志

## v1.0.0
- 初始版本，包含基本的代理收集和合并功能。

## v1.1.0
- 增加了代理节点速度和可用性测试功能。
- 改进了 README 文件的自动更新逻辑。

# 许可协议

本项目采用 MIT 许可协议，详细信息请参见 LICENSE 文件。
