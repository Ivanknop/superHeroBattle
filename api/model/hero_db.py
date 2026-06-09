import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

model_path = os.path.dirname(os.path.realpath(__file__))
api_path = os.path.dirname(model_path)
database_path = os.path.join(api_path, "files", "super_hero.db")


class HeroDB(db.Model):
    __tablename__ = "heroes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    strength = db.Column(db.Float, nullable=False)
    intelligence = db.Column(db.Float, nullable=False)
    hardness = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)
    combat = db.Column(db.Float, nullable=False)
    speed = db.Column(db.Float, nullable=False)
    hp = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def get_name(self):
        return self.name

    def get_strength(self):
        return self.strength

    def get_intelligence(self):
        return self.intelligence

    def get_toughness(self):
        return self.hardness

    def get_power(self):
        return self.power

    def get_combat(self):
        return self.combat

    def get_speed(self):
        return self.speed

    def get_hp(self):
        return self.hp
    def get_total(self):
        return self.total
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "strength": self.strength,
            "intelligence": self.intelligence,
            "hardness": self.hardness,
            "power": self.power,
            "combat": self.combat,
            "speed": self.speed,
            "hp": self.hp,
            "total": self.total
        }

    def __repr__(self):
        return f"<Hero {self.name}>"