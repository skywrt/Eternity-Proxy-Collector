#!/bin/bash

# 下载 base64 编码的节点链接
subscribeclash="https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt"
subscribeV2ray="https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num"

# 创建必要的目录
mkdir -p ./subs ./output

# 清除旧文件
rm -f ./subs/clash_base64.txt ./subs/v2ray_base64.txt ./output/merged_v2ray_sub.txt ./output/merged_clash_sub.yaml

echo "获取订阅..."
wget $subscribeclash -O ./subs/clash_base64.txt
wget $subscribeV2ray -O ./subs/v2ray_base64.txt

echo "解码订阅..."
clash_content=$(cat ./subs/clash_base64.txt | base64 -d)
v2ray_content=$(cat ./subs/v2ray_base64.txt | base64 -d)

# 保存解码后的内容
echo "$clash_content" > ./subs/clash_sub.txt
echo "$v2ray_content" > ./subs/v2ray_sub.txt

# 合并并去重
echo "合并并去重..."
all_nodes=$(echo -e "$clash_content\n$v2ray_content" | sort | uniq)
echo "$all_nodes" > ./subs/all_nodes.txt

# 运行 Python 脚本进行订阅合并和节点测速
echo "运行 Python 脚本进行订阅合并和节点测速..."
python3 list_merge.py

echo "配置文件生成成功"
