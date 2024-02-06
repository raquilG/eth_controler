import os
import json
from .create_config import create_config_file


class Config():
    def __init__(self, file_path):
        self.file_path = file_path

        self.password = ""
        self.time_to_reboot = 0

        #log
        self.log_directory = ""
        self.site_name = ""

        self.admin_mode = 0

        self.load_json()

    def load_json(self):
        try:
            with open(self.file_path, 'r') as json_file:
                json_data = json.load(json_file)

            self.password = json_data["password"]
            self.time_to_reboot = json_data["time_to_reboot"]

            # log
            self.log_directory = json_data["log_directory"]
            self.site_name = json_data["site_name"]
            self.script_name = json_data["script_name"]

            self.admin_mode = json_data["admin_mode"]

            print("Config succesfull load")
        except Exception as ex1:
            print("Failed to load json file", ex1)


def create_config():
    create_config_file()
    json_path = os.path.join("config.json")
    config = Config(json_path)
    return config