class Credentials:
    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        self.credentials_list.append(self)

    def delete_credential(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, name):
        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
