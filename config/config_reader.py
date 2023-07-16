import json


class ConfigReader:
    def __init__(self):
        config_data = self.read_config()

        self.virtual_assistant = config_data["virtual_assistant"]
        self.language = self.virtual_assistant["language"]
        self.voices = config_data["voices"]

    def read_config(self):
        with open("config/config.json") as config_file:
            return json.load(config_file)
