import uuid

import pyodbc  # модуль для работы с базами данных


class EmailArchive:  # класс для работы с архивом электронных писем
    def __init__(self):  # конструктор класса
        # строка подключения к бд
        connection_string = "Driver={SQL Server Native Client 11.0};" \
                            "Server=" + "SOVEYNIK\SQLEXPRESS" + ";" \
                                                                "Database=" + "Email_archive" + ";" \
                                                                                                "Trusted_Connection=yes;"
        # создание объекта подключения
        self.connection = pyodbc.connect(connection_string)
        # создание объекта курсора для выполнения запросов Data Source=SOVEYNIK\SQLEXPRESS;Initial Catalog=KP_IS;Integrated Security=True;Trust Server Certificate = true;
        self.cursor = self.connection.cursor()

    def add_user(self, id, email):  # метод для добавления пользователя
        # sql-запрос для вставки данных в таблицу users
        sql = "INSERT INTO users (id, email) VALUES (?, ?)"
        # выполнение запроса с параметрами
        self.cursor.execute(sql, id, email)
        # сохранение изменений в бд
        self.connection.commit()

    def add_message(self, id, sender_id, subject, date, text):  # метод для добавления сообщения
        # sql-запрос для вставки данных в таблицу messages
        sql = "INSERT INTO messages (id, sender_id, subject, date, text) VALUES (?, ?, ?, ?, ?)"
        # выполнение запроса с параметрами
        self.cursor.execute(sql, id, sender_id, subject, date.strftime('%Y-%m-%d %H:%M:%S'), text)
        # сохранение изменений в бд
        self.connection.commit()

    def add_attachment(self, id, message_id, file_name):  # метод для добавления вложения
        # sql-запрос для вставки данных в таблицу attachments
        sql = "INSERT INTO attachments (id, message_id, file_name) VALUES (?, ?, ?)"
        # выполнение запроса с параметрами
        self.cursor.execute(sql, id, message_id, file_name)
        # сохранение изменений в бд
        self.connection.commit()

    def add_msg(self, msg):  # метод для добавления письма
        # Поиск идентификатора отправителя по email
        sender = self.find_user_by_email(msg.from_)
        if sender is None:
            # Если отправитель не найден, создать нового пользователя с уникальным идентификатором
            sender_id = uuid.uuid4().bytes_le
            self.add_user(sender_id, msg.from_)
        else:
            # Иначе использовать существующий идентификатор
            sender_id = sender.id

        # Проверка наличия письма с таким же sender_id, datetime и subject в базе данных
        query = f"SELECT * FROM messages WHERE sender_id = '{sender_id}' AND date = " \
                f"'{msg.date.strftime('%Y-%m-%d %H:%M:%S')}' AND subject = '{msg.subject}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if result is None:
            # Если такого письма нет, добавить его в базу данных
            # Генерация уникального идентификатора для сообщения
            message_id = uuid.uuid4().bytes_le

            # Добавление сообщения в таблицу messages
            self.add_message(message_id, sender_id, msg.subject, msg.date, msg.text)

            # Добавление вложений в таблицу attachments
            for attachment in msg.attachments:
                # Генерация уникального идентификатора для вложения
                attachment_id = uuid.uuid4().bytes_le
                self.add_attachment(attachment_id, message_id, attachment.filename)
        else:
            # Иначе не добавлять письмо в базу данных и вывести сообщение об ошибке
            print("A message with the same sender_id, datetime and subject already exists in the database.")

    def find_user_by_email(self, email):  # метод для поиска пользователя по email
        # sql-запрос для выборки данных из таблицы users по email
        sql = "SELECT * FROM users WHERE email LIKE ?"
        # выполнение запроса с параметром
        self.cursor.execute(sql, "%" + email + "%")
        # получение результата запроса
        result = self.cursor.fetchone()
        # возврат результата или None если не найден
        return result or None

    def find_user_by_id(self, email):  # метод для поиска пользователя по email
        # sql-запрос для выборки данных из таблицы users по email
        sql = "SELECT * FROM users WHERE id = ?"
        # выполнение запроса с параметром
        self.cursor.execute(sql, email)
        # получение результата запроса
        result = self.cursor.fetchone()
        # возврат результата или None если не найден
        return result or None

    def find_message_by_subject(self, subject):  # метод для поиска сообщения по теме
        # sql-запрос для выборки данных из таблицы messages по subject
        sql = "SELECT * FROM messages WHERE subject LIKE ?"
        # выполнение запроса с параметром (подстановочный символ % для частичного совпадения)
        self.cursor.execute(sql, "%" + subject + "%")
        # получение результата запроса (список всех найденных записей)
        result = self.cursor.fetchall()
        # возврат результата или пустого списка если не найдено
        return result or []

    def find_attachment_by_file_name(self, file_name):  # метод для поиска вложения по имени файла
        # sql-запрос для выборки данных из таблицы attachments по file_name
        sql = "SELECT * FROM attachments WHERE file_name LIKE ?"
        # выполнение запроса с параметром (подстановочный символ % для частичного совпадения)
        self.cursor.execute(sql, "%" + file_name + "%")
        # получение результата запроса (список всех найденных записей)
        result = self.cursor.fetchall()
        # возврат результата или пустого списка если не найдено
        return result or []

    def find_msg(self, sender_id=None, subject=None, text=None, filename=None,
                 datetime=None):  # метод для поиска письма по параметрам
        # Формирование запроса к базе данных с использованием оператора LIKE для поиска подстрок
        query = "SELECT * FROM messages m LEFT JOIN attachments a ON m.id = a.message_id WHERE 1 = 1"
        if sender_id is not None:
            query += f" AND m.sender_id = '{sender_id}'"
        if subject is not None:
            query += f" AND m.subject LIKE '%{subject}%'"
        if text is not None:
            query += f" AND m.text LIKE '%{text}%'"
        if filename is not None:
            query += f" AND a.file_name LIKE '%{filename}%'"
        if datetime is not None:
            query += f" AND m.date = '{datetime}'"

        # Выполнение запроса и получение результата
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        # Преобразование результата в список объектов класса Message
        messages = []
        for row in result:
            message_id = row[0]
            sender_email = self.find_user_by_id(row[1]).email
            subject = row[2]
            date = row[3]
            text = row[4]
            filename = row[6]
            attachments = []
            if filename is not None:
                attachments.append(filename)
            message = [sender_email, subject, date, text, attachments]
            messages.append(message)

        return messages  # возвращение списка сообщений

    def close(self):  # метод для закрытия подключения к бд
        # закрытие курсора и подключения
        self.cursor.close()
        self.connection.close()
