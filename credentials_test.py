import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("github", "12345")

    def test_credentials_instance(self):
        self.assertEqual(self.new_credentials.account_name, "github")
        self.assertEqual(self.new_credentials.account_password, "12345")

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "56789")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_find_credential_by_name(self):
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "56789")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Twitter")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
