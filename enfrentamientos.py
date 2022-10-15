import preparar_lista_personajes 
import random


class User:
    "user was created"
    def __init__(self, name, nick) :
        self._name = name
        self._nick = nick
        self._plays = {}

    def select_hero(self):
        print(preparar_lista_personajes.listar_personajes())
        was_selected = input("ingrese el nombre de alguno de los personajes que aparece en la lista")
        self._character = was_selected
        return print("el personaje elegido ha sido: ", was_selected)

class Hero:
    "hero was created"
    def __init__(self, life, strength, speed, intelligence, hardness, power, combat, total):
        self._life = life
        self._strength =  strength 
        self._speed = speed
        self._intelligence = intelligence
        self._hardness = hardness
        self._power = power
        self._combat = combat
        self._total = total

    def texto_bloqueo(jug):
        frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
        return frases[random.randrange(0,len(frases))]

    def texto_golpe (jug,golpe):
       frases = [f'{jug} produce un daño igual a {golpe}',f'{jug} pega fuerte y quita {golpe} de vida',f'El ataque de {jug} produce {golpe} en su rival',f'Ataque exitoso de {jug} produciendo un daño de {golpe}']
       return frases[random.randrange(0,len(frases))]

class Fight:
    "fight fight fight"
    def __init__(self, user):
        record = []
        
    def select_heros(self):
        print(preparar_lista_personajes.listar_personajes())
        user_selected = input("ingrese el nombre de su héroe de alguno que aparece en la lista")
        opponent_selected = input("ingrese el nombre de su oponente de alguno que aparece en la lista")
        return print(f"{user_selected} vs {opponent_selected}")

    def turno (self,atacante,defensor):
        golpe = 0
        if ((atacante['VEL'].values[0]+random.randrange(0,100)) >= defensor['VEL'].values[0]):
           if (atacante['Total'].values[0]*random.randrange(1,5) > defensor['Total'].values[0]*2):
               golpe = ((atacante['FUE'].values[0]+atacante['COMBATE'].values[0])/2) + random.randrange(0,20)
        return max(golpe,0)

    def ganador (self, jug1,jug2,vida_jug1):
       vencedor = f'Venció {jug2["NOMBRE"].values[0]}' if vida_jug1 < 0 else f'Venció {jug1["NOMBRE"].values[0]}'
       return (f'En la batalla entre {jug1["NOMBRE"].values[0]} y {jug2["NOMBRE"].values[0]}, venció: {vencedor}')

    def the_figth (self,jug1, jug2):
        vida_jug1 = jug1['VIDA'].values[0] 
        vida_jug2 = jug2['VIDA'].values[0]
        jug1_nombre = jug1['NOMBRE'].values[0]
        jug2_nombre = jug2['NOMBRE'].values[0]

        while (vida_jug1 > 0) & (vida_jug2 > 0):
           golpe = self.turno(jug1,jug2)
           if golpe == 0:
                print (Hero.texto_bloqueo(jug1_nombre))
           else: 
                print (Hero.texto_golpe(jug1_nombre,golpe))
                vida_jug2 = vida_jug2 - golpe
           if (vida_jug2 <0):
                print (f'\n{jug2_nombre} fue derrotado\n')
                break
           else:
                print (f'Vida restante de {jug2_nombre}: {vida_jug2}')
        golpe = self.turno (jug2,jug1)
        if golpe == 0:
            print (Hero.texto_bloqueo(jug2_nombre))
        else: 
            print (Hero.texto_golpe(jug2_nombre,golpe))
        vida_jug1 = vida_jug1 - golpe
        if (vida_jug1 <0):
            print (f'\n{jug1_nombre} fue derrotado\n')
        else:
            print (f'Vida restante de {jug1_nombre}: {vida_jug1}')
    ganador(jug1,jug2,vida_jug1)

    
#preparar_dataset()
#personajes = prepararListaPersonajes.listar_personajes()
#jug1 = prepararListaPersonajes.elegir_personaje('Captain America',personajes)
#jug2 = prepararListaPersonajes.elegir_personaje('Batman',personajes)


#print (jug1)
#print (jug2)

one_user = User("Nicolas", "nico")
Fight(one_user)
