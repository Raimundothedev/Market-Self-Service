import json
from pathlib import Path

CONFIG_FILE = Path("config/config.json")

DEFAULT_CONFIG = {
    "currency": "BRL",
    "theme": "dark"
}


def load_config():
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()
    
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def save_config(config):
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_config(config)