import random

class Figth():
    "fight fight fight"

    def __init__(self, figther_one, figther_two):
        self.__fighter_one = figther_one
        self.__fighter_two = figther_two

    def get_fighter_one(self):
        return self.__fighter_one

    def get_fighter_two(self):
        return self.__fighter_two

    def who_hit(self):
        
        if ((self.get_fighter_one().get_speed()+random.randrange(0,100)) >= self.get_fighter_two().get_speed()+random.randrange(0,100)):
            return self.get_fighter_one(), self.get_fighter_two()
        else:
            return self.get_fighter_two(), self.get_fighter_one()

    def figth(self): #las peleas son a muerte o por rounds (?)
        hero_hit, hero_defender = self.who_hit()
        while hero_defender.is_alive():
            if hero_hit.get_total()*random.randrange(1,9) > hero_defender.get_total()*random.randrange(1,9):
                damage = hero_hit.give_hit()
                hero_defender.take_hit(damage)   
            hero_hit, hero_defender = self.who_hit()
        return hero_hit
        

    def texto_bloqueo(jug):
        frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
        return frases[random.randrange(0,len(frases))]

