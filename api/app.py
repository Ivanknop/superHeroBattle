from concurrent.futures.process import _ExceptionWithTraceback
import traceback
from flask import Flask,redirect,url_for,render_template,request
import pruebaDB

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
        return render_template('tabla.html', data=data)
    except:
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
        dataBase = pruebaDB.show(limit=limit, offset=offset)

        return render_template('elegir_personaje.html')
    except:
          return render_template('error404.html')

@app.route("/select",methods=['GET'])
def select():
    name_character = request.args.get("nombre")
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
        hero =pruebaDB.find_hero(name_character,limit=0, offset=0)
        print (hero)
        return render_template ('figth.html',hero=hero)
        
    except:
          
          return render_template(traceback)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="127.0.0.1",port=5000,debug=True)