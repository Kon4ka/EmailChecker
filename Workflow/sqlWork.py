import uuid

import pyodbc  # ������ ��� ������ � ������ ������


class EmailArchive:  # ����� ��� ������ � ������� ����������� �����
    def __init__(self):  # ����������� ������
        # ������ ����������� � ��
        connection_string = "Driver={SQL Server Native Client 11.0};" \
                            "Server=" + "SOVEYNIK\SQLEXPRESS" + ";" \
                                                                "Database=" + "Email_archive" + ";" \
                                                                                                "Trusted_Connection=yes;"
        # �������� ������� �����������
        self.connection = pyodbc.connect(connection_string)
        # �������� ������� ������� ��� ���������� �������� Data Source=SOVEYNIK\SQLEXPRESS;Initial Catalog=KP_IS;Integrated Security=True;Trust Server Certificate = true;
        self.cursor = self.connection.cursor()

    def add_user(self, id, email):  # ����� ��� ���������� ������������
        # sql-������ ��� ������� ������ � ������� users
        sql = "INSERT INTO users (id, email) VALUES (?, ?)"
        # ���������� ������� � �����������
        self.cursor.execute(sql, id, email)
        # ���������� ��������� � ��
        self.connection.commit()

    def add_message(self, id, sender_id, subject, date, text):  # ����� ��� ���������� ���������
        # sql-������ ��� ������� ������ � ������� messages
        sql = "INSERT INTO messages (id, sender_id, subject, date, text) VALUES (?, ?, ?, ?, ?)"
        # ���������� ������� � �����������
        self.cursor.execute(sql, id, sender_id, subject, date.strftime('%Y-%m-%d %H:%M:%S'), text)
        # ���������� ��������� � ��
        self.connection.commit()

    def add_attachment(self, id, message_id, file_name):  # ����� ��� ���������� ��������
        # sql-������ ��� ������� ������ � ������� attachments
        sql = "INSERT INTO attachments (id, message_id, file_name) VALUES (?, ?, ?)"
        # ���������� ������� � �����������
        self.cursor.execute(sql, id, message_id, file_name)
        # ���������� ��������� � ��
        self.connection.commit()

    def add_msg(self, msg):  # ����� ��� ���������� ������
        # ����� �������������� ����������� �� email
        sender = self.find_user_by_email(msg.from_)
        if sender is None:
            # ���� ����������� �� ������, ������� ������ ������������ � ���������� ���������������
            sender_id = uuid.uuid4().bytes_le
            self.add_user(sender_id, msg.from_)
        else:
            # ����� ������������ ������������ �������������
            sender_id = sender.id

        # �������� ������� ������ � ����� �� sender_id, datetime � subject � ���� ������
        query = f"SELECT * FROM messages WHERE sender_id = '{sender_id}' AND date = " \
                f"'{msg.date.strftime('%Y-%m-%d %H:%M:%S')}' AND subject = '{msg.subject}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if result is None:
            # ���� ������ ������ ���, �������� ��� � ���� ������
            # ��������� ����������� �������������� ��� ���������
            message_id = uuid.uuid4().bytes_le

            # ���������� ��������� � ������� messages
            self.add_message(message_id, sender_id, msg.subject, msg.date, msg.text)

            # ���������� �������� � ������� attachments
            for attachment in msg.attachments:
                # ��������� ����������� �������������� ��� ��������
                attachment_id = uuid.uuid4().bytes_le
                self.add_attachment(attachment_id, message_id, attachment.filename)
        else:
            # ����� �� ��������� ������ � ���� ������ � ������� ��������� �� ������
            print("A message with the same sender_id, datetime and subject already exists in the database.")

    def find_user_by_email(self, email):  # ����� ��� ������ ������������ �� email
        # sql-������ ��� ������� ������ �� ������� users �� email
        sql = "SELECT * FROM users WHERE email LIKE ?"
        # ���������� ������� � ����������
        self.cursor.execute(sql, "%" + email + "%")
        # ��������� ���������� �������
        result = self.cursor.fetchone()
        # ������� ���������� ��� None ���� �� ������
        return result or None

    def find_user_by_id(self, email):  # ����� ��� ������ ������������ �� email
        # sql-������ ��� ������� ������ �� ������� users �� email
        sql = "SELECT * FROM users WHERE id = ?"
        # ���������� ������� � ����������
        self.cursor.execute(sql, email)
        # ��������� ���������� �������
        result = self.cursor.fetchone()
        # ������� ���������� ��� None ���� �� ������
        return result or None

    def find_message_by_subject(self, subject):  # ����� ��� ������ ��������� �� ����
        # sql-������ ��� ������� ������ �� ������� messages �� subject
        sql = "SELECT * FROM messages WHERE subject LIKE ?"
        # ���������� ������� � ���������� (�������������� ������ % ��� ���������� ����������)
        self.cursor.execute(sql, "%" + subject + "%")
        # ��������� ���������� ������� (������ ���� ��������� �������)
        result = self.cursor.fetchall()
        # ������� ���������� ��� ������� ������ ���� �� �������
        return result or []

    def find_attachment_by_file_name(self, file_name):  # ����� ��� ������ �������� �� ����� �����
        # sql-������ ��� ������� ������ �� ������� attachments �� file_name
        sql = "SELECT * FROM attachments WHERE file_name LIKE ?"
        # ���������� ������� � ���������� (�������������� ������ % ��� ���������� ����������)
        self.cursor.execute(sql, "%" + file_name + "%")
        # ��������� ���������� ������� (������ ���� ��������� �������)
        result = self.cursor.fetchall()
        # ������� ���������� ��� ������� ������ ���� �� �������
        return result or []

    def find_msg(self, sender_id=None, subject=None, text=None, filename=None,
                 datetime=None):  # ����� ��� ������ ������ �� ����������
        # ������������ ������� � ���� ������ � �������������� ��������� LIKE ��� ������ ��������
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

        # ���������� ������� � ��������� ����������
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        # �������������� ���������� � ������ �������� ������ Message
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

        return messages  # ����������� ������ ���������

    def close(self):  # ����� ��� �������� ����������� � ��
        # �������� ������� � �����������
        self.cursor.close()
        self.connection.close()
