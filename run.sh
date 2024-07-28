#!/bin/bash

# 下载 base64 编码的节点链接
subscribeclash="https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_base64_Sub.txt"
subscribeV2ray="https://raw.githubusercontent.com/hkpc/Autoproxy/main/Long_term_subscription_num"

# 清除旧文件
rm -f ./clash_base64.txt ./v2ray_base64.txt ./clash.yaml ./v2ray.txt

echo "获取订阅..."
wget $subscribeclash -O ./clash_base64.txt
wget $subscribeV2ray -O ./v2ray_base64.txt

echo "解码订阅..."
clash_content=$(cat ./clash_base64.txt | base64 -d)
v2ray_content=$(cat ./v2ray_base64.txt | base64 -d)

# 合并去重
echo "合并并去重..."
all_nodes=$(echo -e "$clash_content\n$v2ray_content" | sort | uniq)

# 保存去重后的节点
echo "$all_nodes" > all_nodes.txt

# 节点检测和测速
check_node_connectivity() {
    local url=$1
    if curl --connect-timeout 5 -s $url >/dev/null; then
        echo "1"
    else
        echo "0"
    fi
}

get_node_speed() {
    local speed=$(speedtest-cli --simple | grep "Download:" | awk '{print $2}')
    if (( $(echo "$speed > 1" | bc -l) )); then
        echo "$speed"
    else
        echo "0"
    fi
}

valid_clash_nodes=""
valid_v2ray_nodes=""

echo "节点检测和测速..."
while read -r node; do
    if [ $(check_node_connectivity "https://www.google.com") -eq 1 ]; then
        speed=$(get_node_speed)
        if (( $(echo "$speed > 1" | bc -l) )); then
            if [[ $node == *"vmess"* ]]; then
                valid_v2ray_nodes="$valid_v2ray_nodes\n$node"
            else
                valid_clash_nodes="$valid_clash_nodes\n$node"
            fi
            echo "有效节点: $node 速度: $speed Mbps"
        fi
    fi
done < all_nodes.txt

# 保存有效节点
echo -e "$valid_v2ray_nodes" | base64 > ./v2ray.txt
echo -e "$valid_clash_nodes" > ./clash.yaml

echo "配置文件生成成功"
