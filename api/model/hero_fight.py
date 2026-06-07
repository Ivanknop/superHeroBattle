import random
from battle_core.fight import Fight
from battle_core.combat_rules import CombatRules

class HeroFight(Fight):
    "fight fight fight"
    def __init__(self, fighter_one, fighter_two, rng=None):
        super().__init__(fighter_one, fighter_two,CombatRules(), rng)

    def turn_text(self, attacker, defender, damage, attacker_luck, defender_luck, defender_initial_hp):
        attacker_name = attacker.get_name()
        defender_name = defender.get_name()

        if self.get_combat_rules().is_automatic_failure(attacker_luck):
            frases = [
                f"¡{attacker_name} falló estrepitosamente!",
                f"¡El golpe de {attacker_name} no encontró su objetivo!",
                f"¡{attacker_name} erró y quedó expuesto!",
            ]
            return random.choice(frases)

        if self.get_combat_rules().is_blocked(attacker, defender, attacker_luck, defender_luck):
            frases = [
                f"¡{defender_name} bloqueó el ataque de {attacker_name} y solo recibió {damage} de daño!",
                f"¡{defender_name} anticipó el golpe y absorbió casi todo el impacto — {damage} de daño!",
                f"¡Defensa magistral de {defender_name}! {attacker_name} apenas le hizo {damage}!",
            ]
            return random.choice(frases)

        if self.get_combat_rules().critical_multiplier(attacker, defender, attacker_luck, defender_luck) > 1:
            frases = [
                f"¡GOLPE CRÍTICO! ¡{attacker_name} destruye a {defender_name} con {damage} de daño!",
                f"¡{attacker_name} desata todo su poder y aplasta a {defender_name} por {damage}!",
                f"¡IMPACTO DEVASTADOR de {attacker_name}! ¡{defender_name} sufre {damage} de daño!",
            ]
            return random.choice(frases)

        if defender_initial_hp <= 0:
            return f"¡{attacker_name} remata a {defender_name} con {damage} de daño!"

        damage_ratio = damage / defender_initial_hp

        if damage_ratio > 0.5:
            frases = [
                f"¡{attacker_name} golpea con furia y arranca {damage} de vida a {defender_name}!",
                f"¡Brutal ataque de {attacker_name} causando {damage} de daño a {defender_name}!",
                f"¡{defender_name} tambalea tras recibir {damage} de daño de {attacker_name}!",
            ]
            return random.choice(frases)

        if damage_ratio < 0.1:
            frases = [
                f"{attacker_name} roza a {defender_name} causando apenas {damage} de daño.",
                f"Golpe débil de {attacker_name} — {defender_name} apenas lo sintió. {damage} de daño.",
                f"{attacker_name} no logra penetrar la defensa de {defender_name}. Solo {damage} de daño.",
            ]
            return random.choice(frases)

        frases = [
            f"¡{attacker_name} conecta un sólido golpe causando {damage} de daño a {defender_name}!",
            f"¡{attacker_name} avanza implacable e inflige {damage} de daño a {defender_name}!",
            f"¡Buen impacto de {attacker_name} sobre {defender_name} por {damage} de daño!",
        ]
        return random.choice(frases)