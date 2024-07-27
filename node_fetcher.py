import base64
import requests

def fetch_and_decode():
    with open('All_Configs_base64_Sub.txt', 'r') as f:
        encoded_data = f.read()
    
    decoded_data = base64.b64decode(encoded_data).decode('utf-8')
    
    with open('decoded_configs.txt', 'w') as f:
        f.write(decoded_data)

if __name__ == "__main__":
    fetch_and_decode()
