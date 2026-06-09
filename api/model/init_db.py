import os
import csv

from app import create_app
from model.hero_db import db
from model.handler_db import insert_hero

script_path = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_path, "files", "lista_de_personajes_estadisticas.csv")

def create_schema():
    db.create_all()

def drop_schema():
    db.drop_all()

def fill():
    with open(csv_path, "r", encoding="utf8") as fi:
        data = list(csv.DictReader(fi))
        for row in data:
            insert_hero(
                row["NOMBRE"],
                row["FUE"],
                row["INT"],
                row["DUR"],
                row["POD"],
                row["VEL"],
                row["VIDA"],
                row["COMBATE"],
                row["Total"]
            )

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        drop_schema()
        create_schema()
        fill()
    print("Base de datos creada y cargada correctamente.")