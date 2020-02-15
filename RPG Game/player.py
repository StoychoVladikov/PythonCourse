from creature import *


class Player(Creature):
    def __init__(self, name, race, hp, attack_power, sword_enchantment_level):
        super().__init__(name, race, hp, attack_power + (sword_enchantment_level/100))
        self.sword_enchantment_level = sword_enchantment_level
        self.creatures_slain = 0

    def get_attack_power(self):
        return self.attack_power

    def get_hp(self):
        return self.hp

    def get_sword_enchantment_level(self):
        return self.sword_enchantment_level

    def get_creatures_slain(self):
        return self.creatures_slain

    def add_slain_creature(self):
        self.creatures_slain = self.creatures_slain + 1

    def set_enchantment_level(self, sword_enchantment_level):
        self.sword_enchantment_level = sword_enchantment_level


    def make_sound(self):
        print("waaaaaaaaa")