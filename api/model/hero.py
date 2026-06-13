from battle_core.entity import Entity
class Hero(Entity):
    "creat a hero"
    def __init__(self, name, vitality, characteristics):
        super().__init__(name, vitality, characteristics)
        
    def offensive_power(self):
        return self.characteristics["strength"] * 0.6 + self.characteristics["combat"] * 0.4 + self.characteristics["power"] * 0.2

    def defensive_power(self):
        return self.characteristics["hardness"] * 0.7 + self.characteristics["strength"] * 0.3

    def initiative(self):
        return self.characteristics["speed"]+ self.characteristics["intelligence"] * 0.5 + self.characteristics["combat"] * 0.5