from creature import *


class Wizard(Creature):
    def __init__(self, name, race, hp, attack_power):
        super().__init__(name, race, hp, attack_power)
        self.has_a_hat = True

    def get_hat(self):
        return self.has_a_hat

    def set_hat(self, has_a_hat):
        self.has_a_hat = has_a_hat

    def check_for_hat(self):
        if self.get_hat():
            self.set_attack_power(self.get_attack_power() + 0.1 * self.get_attack_power())

    def make_sound(self):
        print("fly you fools")

