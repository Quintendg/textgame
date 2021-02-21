from random import randint
import time


def slow_text(string, delay, wait):
    """ Print string letter after letter instead of at once. """

    for char in string:
        print(char, end='')
        time.sleep(delay)
    time.sleep(wait)


class MonsterFightWorld:

    def enter_world(self):
        slow_text("You spot a cave in the distance.\n", 0, 3) 
        slow_text("You walk towards it and decide to enter it.\n", 0, 3)
        slow_text("As you slowly walk through the cave you suddenly approach a round door.\n", 0, 3)
        slow_text("It stops you from going further.\n", 0, 3)
        slow_text("There appears to be a riddle on the door:\n", 0, 3)
        slow_text("\tI am long\n", 0, 0)
        slow_text("\tI haven't got legs\n", 0, 0)
        slow_text("\tI can't walk\n", 0, 0)
        slow_text("\tI can slither\n", 0, 0)
        slow_text("\tI am green\n", 0, 1.5)
        slow_text("What am I?\n", 0, 0)

        guess = input("> ").lower()
        attempts = 0
        while guess != 'snake' and attempts < 2:
            print("Wrong.")
            attempts += 1
            guess = input("> ").lower()

        if guess != 'snake':
            slow_text("You failed too many times.\n", 0, 2)
            slow_text("The environment starts shaking heavily.\n", 0, 3) 
            slow_text("The ceiling collapses on you.\n", 0, 3)
            slow_text("You're dead...", 0.3, 2)
            print("\n")
            return False
        else:
            slow_text("You hear a loud click. The door slowly opens...\n", 0 , 4)
            slow_text("In the distance you see a massive Basilisk sleeping on the floor...\n", 0, 5) 
            print("Disturb it or flee?")
            choice = input("> ").lower()
            if choice == "disturb" or choice == "disturb it":
                slow_text("The Basilisk wakes up and screeches loudly! You are not impressed.\n", 0, 4)
                slow_text("You draw your sword.\n", 0, 3)
                slow_text("Prepare for battle!", 0.1, 2)
            else:
                slow_text("As soon as you turn around to flee you hear a loud screech.\n", 0, 3)
                slow_text("REEEEEEEEEE!!!\n", 0.2, 1.5)
                slow_text("Oh no... it woke up...\n", 0.1, 2) 
                slow_text("It starts slithering towards you...\n", 0, 3)
                slow_text("You draw your sword.\n", 0, 3) 
                slow_text("Prepare for battle!", 0.1, 2)
            
            print("\n\nMonster encountered: Basilisk")
            print("Basilisk special ability: Venom Spew (charge)")
            slow_text("Your special ability: Hypercutter (charge)\n\n", 0, 10)

            legend_hp = 500
            basilisk_hp = 1000
            legend_charged = False
            basilisk_charged = False 
            hp_potions = 3

            while True:
                print("Perform an action:")
                print("1) Attack")
                if legend_charged:
                    print("2) Special ability: Hypercutter")
                else:
                    print("2) Charge")
                print("3) Health potion")
                print("4) Run away")

                action = input("> ")

                if action == "1" or action == "2":
                    if action == "1":
                        dmg_legend = randint(40, 70)
                        basilisk_hp -= dmg_legend
                        slow_text(f"You damage the Basilisk for {dmg_legend} HP!\n", 0, 2)
                    else:
                        if legend_charged:
                            dmg_legend = randint(1,200)
                            basilisk_hp -= dmg_legend
                            slow_text(f"Your Hypercutter ability damages the Basilisk for {dmg_legend} HP!\n", 0, 2)
                            legend_charged = False
                        else:
                            slow_text("You are charging for Hypercutter ability.\n", 0, 2)
                            legend_charged = True

                    slow_text(f"The Basilisk has {basilisk_hp}/1000 HP\n\n", 0, 2)

                    if basilisk_hp <= 0:
                        slow_text("Congratulations, you beat the Basilisk!!!\n", 0, 5)
                        slow_text("You rip off one of the Basilisk's fangs to keep as a trophy.\n", 0, 5)
                        return True #won the game    
                elif action == "3":
                    if hp_potions > 0:
                        if legend_hp <= 300:
                            legend_hp += 200
                            hp_potions -= 1
                            print(f"You drink an HP potion and restore your HP by 200.")
                            print(f"You have {hp_potions} HP potion(s) left.")
                            slow_text(f"Your HP is now {legend_hp}/500\n\n", 0, 3)
                        else:
                            legend_hp = 500
                            hp_potions -= 1
                            print(f"You drink a HP potion and restore your HP by 200.")
                            print(f"You have {hp_potions} HP potion(s) left.")
                            slow_text(f"Your HP is now {legend_hp}/500\n\n", 0, 3)
                    else:
                        slow_text("You haven't any HP potions left!\n\n", 0, 3)
                        continue
                elif action == "4":
                    slow_text("You flee. Coward!!\n", 0, 2)
                    return False
                else:
                    continue

                dmg_basilisk = randint(30, 40)
                venom_spew = randint(1, 10) #1 in 10 chance to cast venom spew
                venom_spew_dmg = 200

                if venom_spew == 1 and basilisk_charged is False:
                    slow_text("Basilisk is charging, it will cast its special ability Venom Spew (200 dmg) next turn!\n", 0, 2)
                    basilisk_charged = True
                elif basilisk_charged:
                    legend_hp -= venom_spew_dmg
                    slow_text("The Baselisk casts Venom Spew and damages you for 200 HP!!\n", 0, 2)
                    basilisk_charged = False
                else:
                    legend_hp -= dmg_basilisk
                    slow_text(f"The Baselisk damages you for {dmg_basilisk} HP!\n", 0, 2)

                if legend_hp <= 0:
                    slow_text("Oh dear... you're dead...\n", 0.2, 3)
                    return False
                else:
                    slow_text(f"You have {legend_hp}/500 HP\n\n", 0 , 2)


class Main:

    def __init__(self):
        self.worlds = {
            'World 1': MonsterFightWorld() 
            # 'World 2': ,
            # 'World 3': ,
            # 'World 4': 
        }
        self.completed = {f'World {i}': False for i in range(1, 5)}

    @staticmethod
    def all_worlds_completed():
        if False in self.completed.values():
            return False
        else:
            return True

    def main_menu(self):
        print("\n--------")
        print("Welcome (back) to the main menu.\n")
        print("Available worlds:")
        print("\tWorld 1: Defeat a tough monster!")
        print("\tWorld 2: ....\n")
        print("Type below the world you want to enter!")
        while True:
            world_choice = input("> ")
            if world_choice not in self.worlds.keys():
                print("Not a world.")
                continue
            else:
                slow_text(f"Entering {world_choice}.\n", 0, 2)
                print("--------")
                break
        return world_choice
    
    def play(self):
        while True:
            world = self.main_menu()
            current_world_completed = self.worlds.get(world).enter_world()
            if self.completed[world] is not True: #assures already completed world stays completed even if player restarts and then loses the level
                self.completed[world] = current_world_completed
            if self.all_worlds_completed():
                slow_text("Congratulations, you beat all worlds! Game ends now.", 0, 3)
                break


if __name__ == "__main__":
    game = Main()
    game.play()