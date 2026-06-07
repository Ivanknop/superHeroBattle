def test_hero_has_expected_characteristics():
    from model.hero import Hero

    hero_characteristics = {
        "strong": 30,
        "hardness": 40, 
        "combat": 50,
        "power": 60,
        "speed": 50,
        "intelligence": 40,
        "strength": 30,
    }    
    rambo = Hero('Rambo', 50, hero_characteristics)

    assert rambo.get_name() == "Rambo"
    assert rambo.get_characteristics()["strong"] == 30
    assert rambo.get_characteristics()["hardness"] == 40
    assert rambo.get_characteristics()["combat"] == 50
    assert rambo.get_characteristics()["power"] == 60
    assert rambo.get_characteristics()["speed"] == 50
    assert rambo.get_characteristics()["intelligence"] == 40
    assert rambo.get_characteristics()["strength"] == 30    
    assert rambo.get_life() == 50

    assert rambo.offensive_power() == 50
    assert rambo.defensive_power() == 37 
    assert rambo.initiative() == 95 