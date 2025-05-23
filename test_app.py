import unittest
from app_secure import is_valid_input

class TestSecureNotes(unittest.TestCase):
    def test_valid_note(self):
        self.assertTrue(is_valid_input("This is a valid note!"))

    def test_invalid_note(self):
        self.assertFalse(is_valid_input(""))
        self.assertFalse(is_valid_input("DROP TABLE USERS;"))

if __name__ == '__main__':
    unittest.main()
