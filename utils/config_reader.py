import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "configs.ini")
config.read(config_path)

def get_base_url():
    return config.get("app", "base_url")

def get_password():
    return config.get("credentials", "password")

def get_usernames():
    users = config.get("users", "usernames")
    return [u.strip() for u in users.split(",")]
