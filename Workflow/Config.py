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
    # ����������� ������
    def __init__(self, file_name):
        # ��������� ��� ����� � ��������
        self.file_name = file_name
        # ������� ������� ��� �������� ��������� ��������� ������
        self.last_data = []
        self.read_list()

    # ����� ��� ������ ������ � json ����
    def write_list(self, list_data):
        # ��������� ���� ��� ������
        with open(self.file_name, "w") as f:
            # ���������� ������ � json ���� � ���������
            json.dump(list_data, f, indent=4)

    # ����� ��� ������ ������ �� json �����
    def read_list(self):
        # ��������� ���� ��� ������
        with open(self.file_name, "r") as f:
            # ������ ������ �� json �����
            list_data = json.load(f)
            # ��������� ������� � ���������� ���������� �������
            self.last_data = list_data
            # ���������� ������
            return list_data