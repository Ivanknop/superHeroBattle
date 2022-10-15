import unittest
from user import User

class TestUser(unittest.TestCase):

    def test_name(self):
        user_one = User ('Nicolás', 'Nico', 'nlascours@hotmail.com')
        self.assertEqual(user_one.get_name(), 'Nicolás')

    def test_nick(self):
        user_one = User ('Nicolás', 'Nico', 'nlascours@hotmail.com')
        self.assertEqual(user_one.get_nick(), 'Nico')

    def test_mail(self):
        user_one = User ('Nicolás', 'Nico', 'nlascours@hotmail.com')
        self.assertEqual(user_one.get_mail(), 'nlascours@hotmail.com') 
    
    '''
    def test_select_character(self):
        user_one = User ('Nicolás', 'Nico', 'nlascours@hotmail.com')
        self.assertEqual(user_one.select_character()['NOMBRE'].values[0], 'Venom' ) '''

    def test_get_character(self):
        user_one = User ('Nicolás', 'Nico', 'nlascours@hotmail.com')
        user_one.select_character()
        self.assertEqual(user_one.get_character()['NOMBRE'].values[0], 'Venom')
       
if __name__ == '__main__':
    unittest.main()