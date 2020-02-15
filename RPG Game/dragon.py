from creature import *


class Dragon(Creature):
    def __init__(self, name, race, hp, attack_power):
        super().__init__(name, race, hp, attack_power)
        self.negates_enchantment_level_of_player = True

    def can_negate_enchantment(self):
        if self.get_hp() < 100:
            self.negates_enchantment_level_of_player = False

    def negate_enchantment(self, player):
        if self.can_negate_enchantment():
            player.set_enchantment_level(0)

    def final_attack(self, player):
        if player.get_hp() <= 100:
            self.set_attack_power(player.get_hp())


    def make_sound(self):
        print("rawrrr")



