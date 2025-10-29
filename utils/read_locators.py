import json
import os

class ReadLocators:
    def __init__(self, page_name):
        base_path = os.path.join(os.path.dirname(__file__), "..", "locators")
        file_path = os.path.join(base_path, f"{page_name}_locators.json")

        with open(file_path, "r") as f:
            locators = json.load(f)

        # Dynamically assign each locator as a tuple (By, value)
        for key, value in locators.items():
            setattr(self, key, tuple(value))
