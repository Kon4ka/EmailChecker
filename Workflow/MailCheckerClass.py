from imap_tools import MailBox, AND, A


class MailChecker:

    def __init__(self, imap_server = None, login = None, password = None, remember_me = False):
        self.triggers = []
        self.imap_server = imap_server
        self.login = login
        self.password = password
        self.mail_server = MailBox(imap_server)
        self.mailbox = None
        if not remember_me:
            self.write_to_login_config()

    def log_in(self, l=None, p=None):
        if l is None:
            l = self.login
        if p is None:
            p = self.password

        try:
            self.mailbox = self.mail_server.login_utf8(l, p, initial_folder='INBOX')
        except Exception as e:
            return -1
        else:
            return 0

    def set_triggers_list(self, triggers: list):

        ##TODO VALIDATION

        if len(triggers) > 0:
            self.triggers = triggers
            return 0
        else:
            return -1  ##TODO ERROR

    def check_email_by_triggers(self):

        result_letters_list = []

        for trigger in self.triggers:
            match trigger[1]:  # Subject / Text...
                case 'From':
                    for msg in self.mailbox.fetch(AND(A(seen=False), from_=trigger[0]), mark_seen=False,
                                                  charset='utf-8'):
                        result_letters_list.append([msg, trigger[2]])
                case 'Subject':
                    for msg in self.mailbox.fetch(AND(A(seen=False), subject=trigger[0]), mark_seen=False,
                                                  charset='utf-8'):
                        result_letters_list.append([msg, trigger[2]])
                case 'Text':
                    for msg in self.mailbox.fetch(AND(A(seen=False), f'TEXT "{trigger[0]}"'), mark_seen=False,
                                                  charset='utf-8'):
                        result_letters_list.append([msg, trigger[2]])
                case 'Attach':
                    for msg in self.mailbox.fetch(A(seen=False), mark_seen=False, charset='utf-8'):
                        if len(msg.attachments) > 0:
                            for att in msg.attachments:
                                if trigger[0].lower() in att.filename.lower():
                                    result_letters_list.append([msg, trigger[2]])

        return result_letters_list

    def write_to_login_config(self):
        pass
