

def test_fighter():
    
    from model.hero_fight import HeroFight
    from model.hero import Hero
    rambo_characteristics = {
        "strong": 300,
        "hardness": 400, 
        "combat": 500,
        "power": 600,
        "speed": 500,
        "intelligence": 400,
        "strength": 300        
    }    
    rambo = Hero('Rambo', 500, rambo_characteristics)

    peuchele_characteristics = {
        "strong": 35,
        "hardness": 30, 
        "combat": 55,
        "power": 80,
        "speed": 80,
        "intelligence": 30,
        "strength": 30        
    }    
    rambo = Hero('Rambo', 50, rambo_characteristics)
    peuchele = Hero ('Peuchele', 20, peuchele_characteristics)
    round = HeroFight(peuchele, rambo)
    assert round.get_fighter_one().get_name() == 'Peuchele'
    assert round.get_fighter_two().get_name() == 'Rambo'   

    events = round.play_turn(player_luck=0, opponent_luck=0)

    assert len(events) == 1
    assert peuchele.is_alive() is False
    assert round.winner().get_name() == "Rambo" 
