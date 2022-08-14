import procesarDatasetPD 
import random

def texto_bloqueo(jug):
    frases = [f'{jug} no pudo dar el golpe',f'{jug} erró',f'{jug} no fue suficientemente veloz',f'Han esquivado a {jug}']
    return frases[random.randrange(0,len(frases))]

def texto_golpe (jug,golpe):
    frases = [f'{jug} produce un daño igual a {golpe}',f'{jug} pega fuerte y quita {golpe} de vida',f'El ataque de {jug} produce {golpe} en su rival',f'Ataque exitoso de {jug} produciendo un daño de {golpe}']
    return frases[random.randrange(0,len(frases))]

def turno (atacante,defensor):
    golpe = 0
    if ((atacante['Speed'].values[0]+random.randrange(0,50)) >= defensor['Speed'].values[0]):
        if (atacante['Total'].values[0]*random.randrange(1,5) > defensor['Total'].values[0]*2):
            golpe = (atacante['Strength'].values[0]/2) + random.randrange(0,20)
    return max(golpe,0)

def ganador (jug1,jug2,vida_jug1):
    vencedor = f'Venció {jug2["Name"].values[0]}' if vida_jug1 < 0 else f'Venció {jug1["Name"].values[0]}'
    return (f'En la batalla entre {jug1["Name"].values[0]} y {jug2["Name"].values[0]}, venció: {vencedor}')


archivo = "lista_de_personajes_estadisticas_pd.csv"
personajes_DC = ['Superman','Batman','Flash III','Aquaman','Robin I','Joker','Penguin','Cyborg','Darkseid','Wonder Woman','Doomsday','Hal Jordan','Dr Manhattan','Lex Luthor','Harley Quinn','Bizarro','Swamp Thing','Punisher','Poison Ivy','Nightwing']
personajes_Marvel =['Thor','Hulk','Wolverine','Magneto','Spider-Man','Iron Man','Captain America','Doctor Strange','Loki','Nick Fury','Professor X','Black Widow','Phoenix','Venom','Scarlet Witch','Kang','Deadpool','Black Panther','Ultron','Thanos']
#preparar_dataset()
data_DC = procesarDatasetPD.crear_lista_personajes(archivo,personajes_DC)
data_Marvel = procesarDatasetPD.crear_lista_personajes(archivo,personajes_Marvel)

jug1 = procesarDatasetPD.elegir_personaje('Superman',data_DC)
jug2 = procesarDatasetPD.elegir_personaje('Thor',data_Marvel)
vida_jug1 = (jug1['Speed'] + jug1['Strength'] + jug1['Intelligence'] + jug1['Durability']*2).values[0]
vida_jug2 = (jug2['Speed'].values + jug2['Strength'] + jug2['Intelligence'] + jug2['Durability']*2).values[0]
jug1_nombre = jug1['Name'].values[0]
jug2_nombre = jug2['Name'].values[0]

while (vida_jug1 > 0) | (vida_jug2 > 0):
    golpe = turno (jug1,jug2)
    if golpe == 0:
        print (texto_bloqueo(jug1_nombre))
    else: 
        print (texto_golpe(jug1_nombre,golpe))
        vida_jug2 = vida_jug2 - golpe
        if (vida_jug2 <0):
            print (f'\n{jug2_nombre} fue derrotado\n')
            break
        else:
            print (f'Vida restante de {jug2_nombre}: {vida_jug2}')
    golpe = turno (jug2,jug1)
    if golpe == 0:
        print (texto_bloqueo(jug2_nombre))
    else: 
        print (texto_golpe(jug2_nombre,golpe))
        vida_jug1 = vida_jug1 - golpe
        if (vida_jug1 <0):
            print (f'\n{jug1_nombre} fue derrotado\n')
            break
        else:
            print (f'Vida restante de {jug1_nombre}: {vida_jug1}')


print (ganador(jug1,jug2,vida_jug1))
print (jug1)
print (jug2)