import unittest
from figth import Figth
from api.hero import Hero

class TestFigth(unittest.TestCase):
    
    def test_hasfigther(self):
        rambo = Hero ('Rambo', 50, 70, 30, 10, 55, 35, 72, 500)
        peuchele = Hero ('Peuchele', 20, 30, 40, 50, 40, 30, 20, 230)
        round = Figth(peuchele, rambo)
        self.assertEqual(round.get_fighter_one().get_name(),'Peuchele')
        self.assertEqual(round.get_fighter_two().get_characteristics()['total'], 500)
        
    def test_fight(self):
        rambo = Hero ('Rambo', 50, 70, 30, 10, 55, 35, 72, 500)
        peuchele = Hero ('Peuchele', 1,1,1,1,1,1,1,1)
        round = Figth(peuchele, rambo)
        round.figth() 
        self.assertEqual(round.figth().get_name(), 'Rambo')
        

    

if __name__ == '__main__':
    unittest.main()
    