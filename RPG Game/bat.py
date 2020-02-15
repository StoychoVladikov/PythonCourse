from creature import *


class Bat(Creature):
    def __init__(self, name, race, hp, attack_power):
        super().__init__(name, race, hp, attack_power)
        self.is_day = "night"

    def make_sound(self):
        print("*screeching*")

    def get_day_or_night(self):
        return self.is_day

    def set_day_or_night(self, day_or_night):
        self.is_day = day_or_night
        if day_or_night == "day":
            self.set_attack_power(0)







