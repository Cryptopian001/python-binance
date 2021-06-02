import json


def load_json_config(json_config_file_path: str, encoding: str = 'utf-8') -> dict:
    with open(json_config_file_path, encoding=encoding) as f:
        return json.load(f)
