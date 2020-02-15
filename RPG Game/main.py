import random
import time

from bat import Bat
from dragon import Dragon
from player import Player
from wizard import *


def main():
    print_header()
    game_loop()


def print_header():
    print("------------------------------------")
    print(" S T U P I D  D U M B  G A M E         ")
    print("------------------------------------")
    print()
    time.sleep(2)
    print("You need to defeat them all.. at any cost .... .... ... .")
    time.sleep(3)


def game_loop():
    creatures = [Dragon('Renfrir', 'Black Dragon', 150, 75),
                 Bat('Squeeky', "Black Bat", 15, 10),
                 Wizard('James Gandalfini', "Wizard", 300, 30),
                 Dragon('Alduin', 'Silver Dragon', 234, 150),
                 ]

    wizard_name = input("Enter your player name: ")
    print()
    time.sleep(1)
    hero = Player(wizard_name, "Human", 250, 25, 15)
    default_hero_hp = 250
    while True:
        active_creature = random.choice(creatures)
        print("A {} has appeared.....".format(active_creature.get_race()))
        time.sleep(2)
        print("His name is {}".format(active_creature.get_name()))
        print()
        time.sleep(2)
        active_creature.print_creature_info()
        print()
        cmd = input("Do you want to [a]ttack, [r]un away, [l]ook around or [s]how your current character stats? \n")
        creature_hp = active_creature.get_hp()
        if cmd == 'a':
            time.sleep(1)
            hero.attack(active_creature)
            if active_creature.is_creature_dead():
                print("{} has been defeated, F in chat bois".format(active_creature.get_name()))
                print()
                time.sleep(3)
                creatures.remove(active_creature)
                hero.add_slain_creature()
            else:
                print("{:0.2f} damage has been done to {}, he's down to {:0.2f} hp".format(hero.get_attack_power(),
                                                                                           active_creature.get_name(),
                                                                                           creature_hp - hero.get_attack_power()))
                print()
                time.sleep(2)
                active_creature.attack(hero)
                if hero.is_creature_dead():
                    print("Your hero is dead, gg wp")
                    time.sleep(1)
                    print("Monsters killed: {}".format(hero.get_creatures_slain()))
                    time.sleep(2)
                    break
        elif cmd == 'r':
            time.sleep(1)
            print('You ran away to recover your health')
            print()
            if hero.get_hp() + 0.25 * hero.get_hp() < default_hero_hp:
                hero.set_hp(hero.get_hp() + 0.25 * hero.get_hp())
            else:
                hero.set_hp(default_hero_hp)
            time.sleep(5)
        elif cmd == 'l':
            time.sleep(1)
            print("You look around and see: ".format(hero.get_name()))
            print("*")
            for c in creatures:
                c.print_creature_info()
                print("*")
                print()
                time.sleep(1.5)
        elif cmd == 's':
            hero.set_hp(hero.get_hp() - active_creature.get_attack_power())
            print("Your hero's current condition: ")
            hero.print_creature_info()
            print("Monsters killed: {}".format(hero.get_creatures_slain()))
            print()
            print("You lost {} hp while wasting your time", active_creature.get_attack_power())
            time.sleep(1)
        else:
            continue

        if not creatures:
            print("MONSTERS KILLED: {}".format(hero.get_creatures_slain()))
            print("YOU WON")
            print("------------------------------------")
            print("           GAME OVER!!!         ")
            print("------------------------------------")
            print()
            break


if __name__ == '__main__':
    main()
