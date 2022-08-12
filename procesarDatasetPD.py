import os
import pathlib
import pandas as pd

def preparar_dataset():
    '''
    Retorna una nueva DB con los personajes escogidos
    '''
    # Nombre del archivo a leer
    archivo_entrada = "superheroes_stats.csv"
    #archivo de salida
    archivo = "lista_de_personajes_estadisticas_pd.csv"
    
    try:
        #abrimos el csv y lo almacenamos como DataFrame en data
        data = pd.read_csv(archivo_entrada)
        #Quitamos las columnas innecesarias
        data = data.drop(columns=['Alignment'])
        #Limpiamos las filas con valores vacíos
        data = data.dropna()
        #Seleccionar solo los que están en la lista solicitada
        #creamos nuevo csv
        data.to_csv(archivo , index=False)
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')

def crear_lista_personajes(nombre_Archivo, una_lista_personajes):
    df = pd.read_csv(nombre_Archivo)
    return df.loc[df['Name'].isin(una_lista_personajes)]

archivo = "lista_de_personajes_estadisticas_pd.csv"
personajes_DC = ['Superman','Batman','Flash III','Aquaman','Robin I','Joker','Penguin','Cyborg','Darkseid','Wonder Woman','Doomsday','Hal Jordan','Elastic Man']
personajes_Marvel =['Thor','Hulk','Wolverine','Magneto','Spider-Man','Iron Man','Captain America','Doctor Strange','Loki','Nick Fury','Professor X','Black Widow','Phoenix','Venom','Scarlet Witch','Kang']
#preparar_dataset()
data_DC = crear_lista_personajes(archivo,personajes_DC)
data_Marvel = crear_lista_personajes(archivo,personajes_Marvel)
print(data_DC)
print(data_Marvel)