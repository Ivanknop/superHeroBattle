from battle_core.combat_rules import CombatRules

class HeroCombatRules(CombatRules):

    def calculate_base_damage(self, attacker, defender):
        type_multiplier = self.type_chart.multiplier_for(attacker, defender)
        if type_multiplier == 0:
            return 0
        raw_damage =attacker.offensive_power() - defender.defensive_power() 
        return max(1, raw_damage * type_multiplier)

    def calculate_turn_damage(self, attacker, defender, attacker_luck, defender_luck):
        if self.is_automatic_failure(attacker_luck):
            return 0
        damage = self.calculate_base_damage(attacker, defender)
        if damage == 0:
            return 0
        if self.is_blocked(attacker, defender, attacker_luck, defender_luck):
            return 1
        damage = damage * self.critical_multiplier(
            attacker,
            defender,
            attacker_luck,
            defender_luck,
        )
        return max(1, round(damage, 2))
