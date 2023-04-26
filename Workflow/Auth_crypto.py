import json
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding


class AuthConfig:
    def __init__(self, filename):
        self.filename = filename

    def create_config(self, username, password):
        key = b'kfmoownmmsggllttnndmnmmsgglleeqq'
        cipher = AES.new(key, AES.MODE_CBC)
        # Шифруем данные с использованием AES
        encrypted_username = cipher.encrypt(Padding.pad(username.encode(), 16))
        encrypted_password = cipher.encrypt(Padding.pad(password.encode(), 16))
        # Создаем словарь с зашифрованными данными и сохраняем его в файл
        config = {"username": encrypted_username.hex(), "password": encrypted_password.hex(), "iv": cipher.iv.hex()}
        with open(self.filename, "w") as f:
            json.dump(config, f)

    def read_config(self):
        with open(self.filename, "r") as f:
            config = json.load(f)
            # Получаем зашифрованные данные из конфига
            encrypted_username = bytes.fromhex(config["username"])
            encrypted_password = bytes.fromhex(config["password"])
            iv = bytes.fromhex(config["iv"])
            # Расшифровываем данные с использованием AES
            cipher = AES.new(b'kfmoownmmsggllttnndmnmmsgglleeqq', AES.MODE_CBC, iv=iv)
            decrypted_username = Padding.unpad(cipher.decrypt(encrypted_username), 16).decode()
            decrypted_password = Padding.unpad(cipher.decrypt(encrypted_password), 16).decode()
            return decrypted_username, decrypted_password

