from preparar_lista_personajes import listar_personajes, look_for_character


class User:
    "user was created"
    def __init__(self, name, nick, mail) :
        self.__name = name
        self.__nick = nick
        self.__mail = mail
        self.__character = None

    def get_name(self):
        return self.__name

    def get_nick(self):
        return self.__nick

    def get_mail(self):
        return self.__mail

    def get_character(self):
        return self.__character
    
    def change_nick(self, new_nick):
        self.__nick = new_nick

    def change_mail(self, new_mail):
        self.__nick = new_mail
    
    def set_character(self, a_character):
        print(a_character)
        self.__character = a_character
        
    
    def select_character(self):
        print(listar_personajes())
        was_selected = input("ingrese el nombre de alguno de los personajes que aparece en la lista: ")
        self.set_character(look_for_character(was_selected)) # guarda el objeto hero
        return self.__character # solo retrona el str 



