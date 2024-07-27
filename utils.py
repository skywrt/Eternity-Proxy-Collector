import base64
import json
import logging

logging.basicConfig(level=logging.INFO)

def log(message: str) -> None:
    logging.info(message)

def base64_decode(data: str) -> str:
    try:
        return base64.b64decode(data).decode('utf-8')
    except Exception as e:
        log(f'Base64 解码失败: {e}')
        return ''

def json_load(data: str) -> dict:
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        log(f'JSON 解码失败: {e}')
        return {}
