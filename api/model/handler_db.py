from model.hero_db import db, HeroDB
from model.hero import Hero
import random

def insert_hero(name, strength, intelligence, hardness, power, speed, hp,combat,total):
    a_hero = HeroDB(
        name=name,
        strength=float(strength),
        intelligence=float(intelligence),
        hardness=float(hardness),
        power=float(power),
        combat=float(combat),
        speed=float(speed),
        hp=float(hp),
        total=float(total)
    )
    db.session.add(a_hero)
    db.session.commit()

    return a_hero

def show(limit=0, offset=0):
    query = HeroDB.query.order_by(HeroDB.name.asc())
    if limit > 0:
        query = query.limit(limit)
        if offset > 0:
            query = query.offset(offset)
    return [_to_domain(p) for p in query.all()]

def find_hero(name) -> Hero:
    hero_db = HeroDB.query.filter(HeroDB.name == name).first()
    return _to_domain(hero_db)

def _to_domain(hero_db):
    characteristics = {
        "strength": hero_db.get_strength(),    
        "speed": hero_db.get_speed(),        
        "intelligence": hero_db.get_intelligence(),
        "hardness": hero_db.get_toughness(), 
        "power": hero_db.get_power(),        
        "combat": hero_db.get_combat(),      
        "total": hero_db.get_total(),
    }
    return Hero(hero_db.get_name(), hero_db.get_hp(), characteristics)

def delete_hero(name):
    hero_db = HeroDB.query.filter(HeroDB.name == name).first()
    if hero_db is None:
        return False
    db.session.delete(hero_db)
    db.session.commit()

    return True

def random_hero_excluding(name):
    heros = HeroDB.query.filter(HeroDB.name != name).all()
    if len(heros) == 0:
        return None
    return _to_domain(random.choice(heros))