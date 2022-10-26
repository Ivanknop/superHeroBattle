from concurrent.futures.process import _ExceptionWithTraceback
import traceback
from flask import Flask, jsonify, redirect,url_for,render_template,request
import handler_db
from figth import Figth
from hero import Hero


app=Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///super_hero.db"
# Asociamos nuestro controlador de la base de datos con la aplicacion
handler_db.db.init_app(app)

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
        data = handler_db.show(limit=limit, offset=offset)
        # Renderizar el temaplate HTML pulsaciones.html
        return render_template('tabla.html', data=data)
    except:
        
        print(jsonify({'trace': traceback.format_exc()}))
        return render_template('error404.html')

@app.route("/elegir_personaje")
def choose_character():
    return render_template('elegir_personaje.html')
    
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
        hero_db = handler_db.find_hero(name_character,limit=0, offset=0)
        rival_db = handler_db.find_hero(name_rival,limit=0, offset=0)
        a_hero = convert_Hero_from_db(hero_db) 
        a_rival = convert_Hero_from_db(rival_db) 
        enfrentamiento = Figth(a_hero,a_rival)
        battle = enfrentamiento.figth()
        data = []
        data.append(hero_db)
        data.append(enfrentamiento.show())
        data.append(battle)
        
        return render_template ('figth.html',hero=data)
        
    except:
          return jsonify({'trace': traceback.format_exc()})  #esta excepción hay que acomodarla




def convert_Hero_from_db (a_hero_db):
    if (type(a_hero_db)== str):
        return Hero(a_hero_db,0,0,0,0,0,0,0,0) 
    else:
        a_hero = Hero(a_hero_db.get_name(), a_hero_db.get_life(), a_hero_db.get_strong(), a_hero_db.get_speed(),a_hero_db.get_intelligence(), a_hero_db.get_toughness(), a_hero_db.get_power(), a_hero_db.get_combat(), a_hero_db.get_total_power())
        return a_hero

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="127.0.0.1",port=5000,debug=True)