#from prepararListaPersonajes import * 
import random


class User:
    "creat an user"

    def __init__(self, name, nick) :
        self.__name = name
        self.__nick = nick
        self.__characters = []
        self.__my_hero = ''
        

    def get_name(self):
        return self.__name

    def get_nick(self):
        return self.__nick

    def get_characters(self):
        return self.__characters

    def add_character(self, *args):
        "Agrega un heroe a la lista de superhéroes elegidos"
        for elem in args:
            self.__characters.append(elem)
    
    def change_nick(self, new_nick):
        self.__nick = new_nick

        
class Fight():
    "fight fight fight"

    def __init__(self, figther_one, figther_two):
        self.__fighter_one = figther_one
        self.__fighter_two = figther_two
        self.__record = []

    def get_fighter_one(self):
        return self.__fighter_one

    def get_fighter_two(self):
        return self.__fighter_two

    def get_record(self):
        return self.__record

    def select_heros(self):
        'selection of the users hero and his opponent'
        'return two objects'

        print(listar_personajes())

        protagonist = input("ingrese el nombre de su héroe de alguno que aparece en la lista")
        user_character = Hero.__init__(protagonist['Nombre'], protagonist['VIDA'], protagonist['FUE'], protagonist['VEL'], protagonist['DUR'], protagonist['POD'], protagonist['COM'], protagonist['TOTAL'])
        User.add_character(user_character)
        antagonist = input("ingrese el nombre de su oponente de alguno que aparece en la lista")
        rival = Hero.__init__(antagonist['Nombre'], antagonist['VIDA'], antagonist['FUE'], antagonist['VEL'], antagonist['DUR'], antagonist['POD'], antagonist['COM'], antagonist['TOTAL'])
        User.add_character(user_character)
        
        return user_character, rival

    def texto_bloqueo(jug):
        frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
        return frases[random.randrange(0,len(frases))]

'''# Pruebo el Objeto User
nico = User("Nicolás", "Nico")
print(nico.get_name())
nico.add_character("Peuchele", "Bambini")
print(nico.get_characters())
print(nico.get_nick())
nico.change_nick("Baskito")
print(nico.get_nick())


# Pruebo el Objeto Hero
peuchele = Hero ('Peuchele', 20, 30, 40, 50, 40, 30, 20, 230)
print(peuchele.get_life())
peuchele.take_hit(10)
print(peuchele.get_life())
peuchele.energy_wins(30)
print(peuchele.get_life())

# Pruebo el Objeto Figth
one_figth= Fight()
one_figth.select_heros()'''