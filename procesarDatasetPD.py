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
        #abrimos el csv y lo almacenamos como DataFrame en df
        df = pd.read_csv(archivo_entrada)
        #Quitamos las columnas innecesarias
        df = df.drop(columns=['Alignment'])
        #Limpiamos las filas con valores vacíos
        df = df.dropna()
        #Renombramos las columnas
        df = df.rename(columns={'Name':'NOMBRE','Intelligence':'INT','Strength':'FUE','Speed':'VEL','Durability':'DUR','Power':'POD','Combat':'COMBATE'})
        df['VIDA'] = df['VEL']+ df['FUE'] + df['INT'] + df['DUR']
        #creamos nuevo csv
        df.to_csv(archivo , index=False)
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')

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

preparar_dataset()