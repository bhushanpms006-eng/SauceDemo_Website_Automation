import configparser
import os

# Build the absolute path to configs/configs.ini
config_path = os.path.join(os.path.dirname(__file__), "..", "configs", "configs.ini")

config = configparser.ConfigParser()
config.read(config_path)


def get_browser_name():
    """Returns browser name from configs.ini"""
    return config.get("DEFAULT", "browser", fallback="chrome")


def get_base_url():
    """Returns base URL from configs.ini"""
    return config.get("DEFAULT", "base_url", fallback="https://www.saucedemo.com/")


def get_username():
    """Returns username from configs.ini"""
    return config.get("CREDENTIALS", "username", fallback="standard_user")


def get_password():
    """Returns password from configs.ini"""
    return config.get("CREDENTIALS", "password", fallback="secret_sauce")
