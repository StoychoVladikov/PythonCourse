class Creature:
    def __init__(self, name, race, hp, attack_power):
        self.name = name
        self.race = race
        self.attack_power = attack_power
        self.hp = hp

    def get_name(self):
        return self.name

    def get_race(self):
        return self.race

    def get_hp(self):
        return self.hp

    def get_attack_power(self):
        return self.attack_power

    def set_hp(self, hp):
        self.hp = hp

    def set_attack_power(self, attack_power):
        self.attack_power = attack_power

    def print_creature_info(self):
        print("Name: " + self.get_name())
        print("Race: " + self.get_race())
        print("HP: " + str(self.get_hp()))
        print("Attack Power: " + str(self.get_attack_power()))

    def attack(self, creature):
        creature.set_hp(creature.get_hp() - self.get_attack_power())

    def is_creature_dead(self):
        if self.get_hp() <= 0:
            return True
        else:
            return False
