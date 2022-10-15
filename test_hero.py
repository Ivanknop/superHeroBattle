import unittest
from hero import Hero

class TestHero(unittest.TestCase):
    def test_getters(self):
        peuchele = Hero ('Peuchele', 20, 30, 40, 50, 40, 30, 20, 230)
        self.assertEqual(peuchele.get_name(),'Peuchele')
        self.assertEqual(peuchele.get_combat(), 20)
        self.assertEqual(peuchele.get_life(), 20)
        self.assertEqual(peuchele.get_total(), 230)

    def test_isalive(self):
        peuchele = Hero ('Peuchele', 20, 30, 40, 50, 40, 30, 20, 230)
        self.assertTrue(peuchele.is_alive())
        peuchele.take_hit(50)
        self.assertEqual(peuchele.get_life(), 0)
        self.assertFalse(peuchele.is_alive())
        
if __name__ == '__main__':
    unittest.main()
        
        