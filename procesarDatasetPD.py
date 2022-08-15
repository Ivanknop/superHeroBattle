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

preparar_dataset()