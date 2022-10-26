class Hero:
    "creat a hero"
    def __init__(self, name, life, strength, speed, intelligence, hardness, power, combat, total):
        self.characteristics = {'life':life,'strength': strength, 'speed':speed, 'intelligence': intelligence, 'hardness':hardness, 'power':power, 'combat':combat,'total':total}
        self.__name = name

    def get_name(self):
        return self.__name

    def get_characteristics(self):
        return self.characteristics

    def get_life(self):
        return max(self.get_characteristics()['life'], 0) 

    def give_hit(self):
        return (self.get_characteristics()['combat'] + self.get_characteristics()['power'])/2

    def take_hit(self, a_hit): # no creo que sea un método del objeeto
       'subtracts the corresponding amount of life produced by the hit'
       self.get_characteristics()['life'] -= a_hit

    def energy_wins(self, energy): # no creo que sea un método del objeto
        self.get_characteristics()['life'] += (self.get_characteristics()['life'] * energy)/100
    
    def is_alive(self):
        return self.get_life() > 0

    def __str__(self): #está mal, acomodarlo
         return str(self.characteristics)
