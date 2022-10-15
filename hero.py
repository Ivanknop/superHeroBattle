class Hero:
    "creat a hero"
    def __init__(self, name, life, strength, speed, intelligence, hardness, power, combat, total):
        self.__name = name
        self.__life = life
        self.__strength =  strength 
        self.__speed = speed
        self.__intelligence = intelligence
        self.__hardness = hardness
        self.__power = power
        self.__combat = combat
        self.__total = total

    def get_name(self):
        return self.__name

    def get_life(self):
        return max(self.__life, 0) 

    def get_strength(self):
        return self.__strength

    def get_speed(self):
        return self.__speed

    def get_intelligence(self):
        return self.__intelligence

    def get_hardness(self):
        return self.__hardness    

    def get_power(self):
        return self.__power

    def get_combat(self):
        return self.__combat

    def get_total(self):
        return self.__total

    def give_hit(self):
        return (self.get_combat() + self.get_power())/2

    def take_hit(self, a_hit): # no creo que sea un método del objeeto
       'subtracts the corresponding amount of life produced by the hit'
       self.__life -= a_hit

    def energy_wins(self, energy): # no creo que sea un método del objeto
        self.__life += (self.__life * energy)/100
    
    def is_alive(self):
        return self.get_life() > 0

    def texto_bloqueo(jug):
        frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
        return frases[random.randrange(0,len(frases))]

    def texto_golpe (jug,golpe):
       frases = [f'{jug} produce un daño igual a {golpe}',f'{jug} pega fuerte y quita {golpe} de vida',f'El ataque de {jug} produce {golpe} en su rival',f'Ataque exitoso de {jug} produciendo un daño de {golpe}']
       return frases[random.randrange(0,len(frases))]