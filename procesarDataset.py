import csv
import os
import pathlib

def convertir(lista_de_personajes):
    '''
    Retorna una nueva DB con los personajes escogidos
    '''
    # Direccion del archivo a leer
    directorio_entrada = pathlib.Path(__file__).parent.absolute()
    # Nombre del archivo a leer
    archivo_entrada = "superheroes_stats.csv"

    # Direccion destino del nuevo dataset
    directorio_salida = pathlib.Path(__file__).parent.absolute()
    # Nombre del archivo a escribir/crear
    archivo = "lista_de_personajes_estadisticas.csv"
    
    try:
        # Abro el archivo a leer y lo cargo  en una lista sin el encabezado
        with open(os.path.join(directorio_entrada, archivo_entrada), encoding='utf_8') as data:
            csvreader = csv.reader(data, delimiter=',')
            encabezado, data_file_input = next(csvreader), list(csvreader)

        # sobre escribo el header
        nuevo_encabezado = ['Nombre', 'Inteligencia','Fuerza','Velocidad','Dureza','Poder','Combate']

        # Genero una lista de listas con las columnas necesarias usando listcomprehension
        new_data = [[ linea[0],linea[2],linea[3], linea[4],linea[5],linea[6]] for linea in data_file_input if linea[0] in lista_de_personajes]
        # Abro/creo y escribo el archivo con los nuevos datos
        try:
            with open(os.path.join(directorio_salida, archivo), 'w', newline='',
                    encoding='utf_8') as new_dataset:
                csvwriter = csv.writer(new_dataset, delimiter=',')
                csvwriter.writerow(nuevo_encabezado)
                csvwriter.writerows(new_data)
        except:
            pass
    except FileNotFoundError:
        print('ERROR: No se ha encontrado el archivo.')

    return new_data
personajes_DC = ['Superman','Batman','Flash','Aquaman','Robin','Joker','Penguin']
personajes_Marvel =['Thor','Hulk','Wolverine','Magneto','Spider-Man','Iron Man','Captain America']
nueva_data = convertir(personajes_DC)
print (nueva_data)
