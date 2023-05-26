import json


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = None
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)


class JsonConverter:
    # конструктор класса
    def __init__(self, file_name):
        # сохраняем имя файла в атрибуте
        self.file_name = file_name
        # создаем атрибут для хранения последних считанных данных
        self.last_data = []
        self.read_list()

    # метод для записи списка в json файл
    def write_list(self, list_data):
        # открываем файл для записи
        with open(self.file_name, "w") as f:
            # записываем список в json файл с отступами
            json.dump(list_data, f, indent=4)

    # метод для чтения списка из json файла
    def read_list(self):
        # открываем файл для чтения
        with open(self.file_name, "r") as f:
            # читаем список из json файла
            list_data = json.load(f)
            # обновляем атрибут с последними считанными данными
            self.last_data = list_data
            # возвращаем список
            return list_data