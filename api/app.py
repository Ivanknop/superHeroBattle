from concurrent.futures.process import _ExceptionWithTraceback
import traceback
from flask import Flask, jsonify, redirect,url_for,render_template,request
from pruebaDB import show
import pruebaDB, figth as figth
from hero import Hero


app=Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///super_hero.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
pruebaDB.db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta que se ingresa por la ULR 127.0.0.1:5000/pulsaciones
@app.route("/personajes")
def personajes():
    try:
        # Obtener de la query string los valores de limit y offset
        limit_str = str(request.args.get('limit'))
        offset_str = str(request.args.get('offset'))
        limit = 0
        offset = 0
        if(limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)
        if(offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)
        # Obtener el reporte
        data = pruebaDB.show(limit=limit, offset=offset)
        # Renderizar el temaplate HTML pulsaciones.html
        #print("Renderizar tabla.html")
        print(data)
        return render_template('tabla.html', data=data)
    except:
        
        print(jsonify({'trace': traceback.format_exc()}))
        return render_template('error404.html')

@app.route("/elegir_personaje")
def choose_character():
    try:
        limit_str = str(request.args.get('limit'))
        offset_str = str(request.args.get('offset'))
        limit = 0
        offset = 0
        if(limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)
        if(offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)
        # Obtener el reporte
        dataBase = pruebaDB.show(limit=limit, offset=offset) #hasta acá parece ser código que no sirve

        return render_template('elegir_personaje.html')
    except:
          return jsonify({'trace': traceback.format_exc()})

@app.route("/select",methods=['GET'])
def select():
    name_character = request.args.get("heroe")
    name_rival = request.args.get("rival")
    try:
        limit_str = str(request.args.get('limit'))
        offset_str = str(request.args.get('offset'))
        limit = 0
        offset = 0
        if(limit_str is not None) and (limit_str.isdigit()):
            limit = int(limit_str)
        if(offset_str is not None) and (offset_str.isdigit()):
            offset = int(offset_str)
        # Obtener el reporte
        hero_db = pruebaDB.find_hero(name_character,limit=0, offset=0)
        rival_db = pruebaDB.find_hero(name_rival,limit=0, offset=0)
        a_hero = Hero(hero_db.get_name(), hero_db.get_life(), hero_db.get_strong(), hero_db.get_speed(),hero_db.get_intelligence(), hero_db.get_toughness(), hero_db.get_power(), hero_db.get_combat(), hero_db.get_total_power())
        a_rival = Hero(rival_db.get_name(), rival_db.get_life(), rival_db.get_strong(), rival_db.get_speed(),rival_db.get_intelligence(), rival_db.get_toughness(), rival_db.get_power(), rival_db.get_combat(), rival_db.get_total_power())
        cuadro_de_caracteristicas = figth.Figth(a_hero,a_rival)
        data = []
        data.append(hero_db)
        data.append(cuadro_de_caracteristicas.show())
        
        return render_template ('figth.html',hero=data)
        
    except:
          return jsonify({'trace': traceback.format_exc()})  #esta excepción hay que acomodarla, al no elegir nombre---> rompe

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="127.0.0.1",port=5000,debug=True)