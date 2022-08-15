import procesarDatasetPD 
import pandas as pd


def crear_lista_personajes(nombre_Archivo, una_lista_personajes):
    df = pd.read_csv(nombre_Archivo)  
    #Correjir características de algunos personajes
    df.at[162,'VEL']=90
    df.at[376,'INT']=70
    df.at[376,'VEL'] = 90
    df.at[381,'VEL'] = 50
    df.at[419,'FUE'] = 65
    df.at[419,'VEL'] = 60
    df.at[301,'INT']=150
    #setteamos el poder total con una fórmula propia
    fuerza = df['FUE']
    velocidad = df['VEL']
    inteligencia = df['INT']
    poder = df['POD']
    combate = df['COMBATE']
    df['Total'] = (fuerza+velocidad+combate)*(inteligencia+poder)
    return df.loc[df['NOMBRE'].isin(una_lista_personajes)]

def elegir_personaje(nombre_personaje,data):
    personaje = data.loc[data.NOMBRE == nombre_personaje]
    return personaje

def listar_personajes():
    archivo = "lista_de_personajes_estadisticas_pd.csv"
    personajes = ['Superman','Chuck Norris','Batman','Flash III','Aquaman','Robin I','Joker','Penguin','Cyborg','Darkseid','Wonder Woman','Doomsday','Hal Jordan','Dr Manhattan','Goku','Lex Luthor','Harley Quinn','Bizarro','Swamp Thing','Punisher','Poison Ivy','Nightwing','Thor','Hulk','Wolverine','Magneto','Spider-Man','Iron Man','Captain America','Doctor Strange','Loki','Nick Fury','Professor X','Black Widow','Phoenix','Venom','Scarlet Witch','Kang','Deadpool','Black Panther','Ultron','Thanos']

    return crear_lista_personajes(archivo,personajes)
