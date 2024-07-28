#!/bin/bash

currentdate=$(date +%Y%m%d)
currentmonth=$(date +%Y%m)
currentmonths=$(date +%m)
currentyears=$(date +%Y)

# 下载 base64 编码的节点链接
subscribeclash="https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt"
subscribeV2ray="https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num"

if [ -f "./clash.yaml" ]; then
  rm ./clash.yaml
fi

if [ -f "./v2ray.txt" ]; then
  rm ./v2ray.txt
fi

echo "获取订阅..."
wget $subscribeclash -O ./clash_base64.txt
wget $subscribeV2ray -O ./v2ray_base64.txt

echo "生成配置文件并检查节点..."
python3 check_nodes.py

echo "获取订阅成功"
echo "希望你有美好的一天~"
echo "再见~"
