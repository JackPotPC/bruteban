import os

class Parser:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}

    def load(self):
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Конфигурационный файл не найден.")
        with open(self.config_file, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=")
                    key = key.strip()
                    valute = value.strip()
                    self.config[key] = self.parser(value)

    def parser(self, value):
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            list_items = value[1:-1].split(",")
            return [item.strip() for item in list_items if item.strip()]
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        try:
            return int(value)
        except ValueError:
            return value