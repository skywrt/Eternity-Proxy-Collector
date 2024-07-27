import requests
import os
import base64

def initialize_files(file_paths):
    # Ensure that the directories exist
    for path in file_paths.values():
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Create or clear the files
        open(path, "w").close()

def download_and_process_config(url, file_paths):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we raise an error for failed requests
    content = response.text

    data = {"vmess": [], "vless": [], "trojan": [], "ss": [], "ssr": []}
    for line in content.splitlines():
        if line.startswith("vmess"):
            data["vmess"].append(line)
        elif line.startswith("vless"):
            data["vless"].append(line)
        elif line.startswith("trojan"):
            data["trojan"].append(line)
        elif line.startswith("ss"):
            data["ss"].append(line)
        elif line.startswith("ssr"):
            data["ssr"].append(line)

    # Write data to files
    for protocol, lines in data.items():
        if protocol == "vmess":
            with open(file_paths[protocol], "w") as f:
                f.write("\n".join(lines) + "\n")
        else:
            encoded_data = base64.b64encode("\n".join(lines).encode("utf-8")).decode("utf-8")
            with open(file_paths[protocol], "w") as f:
                f.write(encoded_data + "\n")

def main():
    base_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
    file_paths = {
        "vmess": os.path.join(base_path, 'Splitted-By-Protocol/vmess.txt'),
        "vless": os.path.join(base_path, 'Splitted-By-Protocol/vless.txt'),
        "trojan": os.path.join(base_path, 'Splitted-By-Protocol/trojan.txt'),
        "ss": os.path.join(base_path, 'Splitted-By-Protocol/ss.txt'),
        "ssr": os.path.join(base_path, 'Splitted-By-Protocol/ssr.txt')
    }

    initialize_files(file_paths)
    url = "https://raw.githubusercontent.com/hkpc/V2ray-Configs/main/All_Configs_Sub.txt"
    download_and_process_config(url, file_paths)

if __name__ == "__main__":
    main()
