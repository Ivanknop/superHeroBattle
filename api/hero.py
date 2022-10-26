class Hero:
    "creat a hero"
    def __init__(self, name, life, strength, speed, intelligence, hardness, power, combat, total):
        self.characteristics = {'life':life,'strength': strength, 'speed':speed, 'intelligence': intelligence, 'hardness':hardness, 'power':power, 'combat':combat,'total':total}
        self.__name = name
        self.__life = life

    def get_name(self):
        return self.__name

    def get_characteristics(self):
        return self.characteristics

    def get_life(self):
        return max(self.get_characteristics(), 0) 

    def give_hit(self):
        return (self.get_combat() + self.get_power())/2

    def take_hit(self, a_hit): # no creo que sea un método del objeeto
       'subtracts the corresponding amount of life produced by the hit'
       self.__life -= a_hit

    def energy_wins(self, energy): # no creo que sea un método del objeto
        self.__life += (self.__life * energy)/100
    
    def is_alive(self):
        return self.get_life() > 0

    def __str__(self): #está mal, acomodarlo
         return str(self.characteristics)

    def texto_bloqueo(jug):
        frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
        return frases[random.randrange(0,len(frases))]

    def texto_golpe (jug,golpe):
       frases = [f'{jug} produce un daño igual a {golpe}',f'{jug} pega fuerte y quita {golpe} de vida',f'El ataque de {jug} produce {golpe} en su rival',f'Ataque exitoso de {jug} produciendo un daño de {golpe}']
       return frases[random.randrange(0,len(frases))]

