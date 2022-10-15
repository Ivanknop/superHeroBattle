import sqlite3
import csv
import os


 # Direccion del archivo a leer
name_input = os.path.join("superHeroBattle\src\dataset_output", "lista_de_personajes_estadisticas_pd.csv")
base_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(os.path.dirname(base_path), name_input)
print(file_path)


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('superhero.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

 # Ejecutar una query
    c.execute("""
         CREATE TABLE superhero(
         [id] INTEGER PRIMARY KEY AUTOINCREMENT,
         [nombre] TEXT NOT NULL,
         [inteligencia] FLOAT NOT NULL,
         [fuerza] FLOAT NOT NULL,
         [velocidad] FLOAT NOT NULL,
         [dureza] FLOAT NOT NULL,
         [poder] FLOAT NOT NULL,
         [combate] FLOAT NOT NULL,
         [total] FLOAT NOT NULL,
         [vida] FLOAT NOT NULL
     );
     """)
    # Salvo los cambios realizados en la DB 
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()

def fill():
    conn = sqlite3.connect('superhero.db')
    c = conn.cursor()
    #Abrimos el archivo CSV
    with open(os.path.join(file_path), encoding='utf_8') as data:
           csvreader = csv.reader(data, delimiter=',')
           #header, data_file_input = next(csvreader), list(csvreader)

        #Llenamos la BD con los datos del CSV
    for row in csvreader:
        c.execute("INSERT INTO superhero VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    #Muestro las filas guardadas en la tabla
    for row in c.execute('SELECT * FROM superhero'):
         print(row)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

if __name__ == '__main__':
    
    create_schema()
    fill()