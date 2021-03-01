from random import randint
import time


def slow_text(string, delay, wait):
    """ Print string letter after letter instead of at once. """

    for char in string:
        print(char, end='')
        time.sleep(delay)
    time.sleep(wait)


class GamesNight:

    def enter_world(self):
        slow_text("Welcome to a game of randomized dice rolling.\n", 0, 3)
        slow_text("As you may input a number between 1 and 12, the output will be random. \n", 0, 3)
        slow_text("That means, both you and the computer have as much chance, or is there? \n", 0, 3)
        slow_text("If you crack the mathematics behind the game, success will be on your side! \n", 0, 3)

        points = 0
        while points < 80:
            try:
                player = int(input("Pick a number between 1 and 12: "))
                if not 0 < player < 13:
                    print("A number between 1 and 12!")
                    continue
            except:
                print("Provide a number!")
                continue
            player_throw = randint(1, player)
            player_throw2 = 0
            if player_throw <= 2:
                player_throw2 += 11
            elif player_throw > 6: 
                player_throw2 += 1
            else:
                player_throw2 += 5

            computer = randint(1, 12)
            if player_throw2 == computer:
                print("Its a tie")
            elif player_throw2 > computer:
                print(f"You rolled a {player_throw2} against {computer}, and scored 10 points.")
                points += 10
                if points > 80:
                    print("Great job! You just beat the computer in a dice game.")
                else:
                    print("Go again!")
            else:
                print(f"You just threw {player_throw2} and lost against the computer {computer}.")
        else:
            slow_text("You completed the first stage!\n\n", 0, 3)
            name = input("What's your name? ") 
            slow_text(f"Very well {name}, now things will get a bit more difficult.\n", 0, 3)
            slow_text("You just enterd the second arena!\n", 0, 3)
            slow_text("Welcome to the Quiz, where you have to answer 5 out of 6 questions correct.\n", 0, 3)
            slow_text("Remember, the following questions are almost all answered with True or False.\n", 0, 3)
            slow_text(f"\nOkay {name}, let's get started!\n", 0, 3) 

            t = ["True", "true", "T", "t"]
            f = ["False", "false", "F", "f"]
            questions = [
                ("\nThe capital of iceland is Reykjavik.", t),
                ("\nThe elephant is the biggest land animal.", t),
                ("\n97 is a prime number.", t),
                ("\nComplete the following sequence: 16 - 4 - 8 - 12 - 3 - 6 - ...", ["9"]),
                ("\nThe number of inhabitants for Germany, Spain and France together exceeds the number of inhabitants in Nigeria.", f),
                ("\nThe world largest nation without any ocean boundaries is Kazachstan.", t)
            ]
            correct = 0 
            for q, a in questions:
                print(q)
                choice = input("> ")
                if choice in a:
                    correct += 1

            slow_text(f"\nYou're finished, {name}. You got {correct} out of 6 correct.\n", 0, 2)
            time.sleep(2)
            if correct >= 4:
                slow_text("Well done.\n", 0, 2)
                slow_text("You complete the second and final stage!\n", 0, 2)
                return True
            else:
                slow_text(f"You come {4 - correct} short. Try better next time!\n", 0, 2)
                return False


class FootballFinal:

    def enter_world(self):
        slow_text("Reporter:\n", 0, 2)
        slow_text("Welcome to the final of the Champions League on this beautiful day!\n", 0, 3)
        slow_text("Today, the two teams will battle for eternal glory.\n", 0, 3)
        slow_text("The match ended in 2-2 in the regular time.\n", 0, 2)
        slow_text("Now, penalties are needed to decide who will be the winner!\n", 0, 3)
        slow_text("The first team to take a penalty is:\n", 0, 2)
        
        print("\nChoose your favourite players for team 1 and 2: (please enter the numbers of the player)")
        print("1: \tLionel Messi")
        print("2: \tCristiano Ronaldo")
        print("3: \tRobert Lewandowski")
        print("4: \tGeorginio Wijnaldum")
        print("5: \tKevin de Bruyne")
        
        # Choosing team
        teams = ["Barcelona", "Juventus", "Bayern Munchen", "Liverpool", "Manchester City"]
        while True:
            try:
                print("Team 1:")
                team1 = int(input("> "))
                print("Team 2:")
                team2 = int(input("> "))
            except:
                print("Provide a number and not characters.")
                continue

            if 0 < team1 < 6 and 0 < team2 < 6 and team2 != team1:
                team1_name = teams[team1 - 1]
                print(f"Your team is {team1_name}!")
                team2_name = teams[team2 - 1]
                print(f"The other team is {team2_name}!")
                break
            else:
                print("Please enter a number between 1 and 5 for both teams, and make sure teams are different.")
                continue
         
        slow_text(f"\nSo, can {team1_name} handle the pressure better than {team2_name}?\n", 0, 5)
        print("-"*10)
        
        # Players need to answer questions correct to have a higher chance to score a penalty
        slow_text("Answer questions correct to have a higher chance to score a penalty.\n", 0, 3)
        slow_text("The team which manages to score the most penalties is the winner!\n", 0, 3)
        slow_text("All answers are 'True' or 'False'.\n", 0, 3)

        questions = [
            ("\nQuestion 1:\n\nCOVID-19 is an abbreviation for Corona Virus Disease 2019", "True"),
            ("\nQuestion 2:\n\nM&M stands for Mars and Moordale", "False"),
            ("\nQuestion 3:\n\nThere are two parts of the body that can't heal themselves", "False"),
            ("\nQuestion 4:\n\nBananas are curved because they grow upwards towards the sun", "True"),
            ("\nQuestion 5:\n\nIn the 'normal' Harry Potter story, there are 7 books and 8 movies", "True"),
            ("\nQuestion 6:\n\nThe small intestine is about 7 meters long", "True"),
            ("\nQuestion 7:\n\nCoffee will dehydrate you", "False"),
            ("\nQuestion 8:\n\nSydney is the capital of Australia", "False"),
            ("\nQuestion 9:\n\nCarrots are good for your eyes", "True"),
            ("\nQuestion 10:\n\nLightning never strikes the same place twice", "False"),
            ("\nQuestion 11:\n\nPeople in Japan eat Kentucky Fried Chicken for Christmas dinner", "True")
        ]
        team1_score = 0
        team2_score = 0
        for q, a in questions:
            t1_score, t2_score = self.scores_question(team1_name, team2_name, team1_score, team2_score, q, a)
            team1_score = t1_score
            team2_score = t2_score

        if team1_score > team2_score:
            slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
            return True
        else:
            slow_text(f"You lost! {team2_name} wins the Champions League after penalties...\n", 0, 5)
            return False
            
    def scores_question(self, team1_name, team2_name, team1_score, team2_score, question, answer):
        """ Gives a score to a team depending on correct answering of a question. 
        Gives also a score to the opponents team"""
    
        question_right = randint(1, 10)
        question_wrong = randint(1, 6) #chance to score a penalty when question is wrong
        chance_opponent = randint(1, 2) #chance for the opponent to score
        true = ["True", "true", "T", "t"]
        false = ["False", "false", "F", "f"]
        
        print(question)

        while True:
            choice = input("> ")

            if choice in true or choice in false:
                if choice in true:
                    choice = "True"
                else:
                    choice = "False"

                if choice == answer:
                    if question_right <= 8:
                        team1_score += 1
                        slow_text("Correct!\n", 0, 2)
                        slow_text(f"{team1_name} manages to score the penalty!!\n", 0, 3)
                        slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
                        break
                    else:
                        team1_score += 0
                        slow_text("Correct!\n", 0, 2)
                        slow_text("Auch, that is an unlucky shot! He misses..\n", 0, 3)
                        slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
                        break
                else:
                    if question_wrong < 2:
                        team1_score += 1
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text(f"However, {team1_name} manages to score a really lucky goal!\n", 0, 3)
                        slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
                        break
                    else:
                        team1_score += 0
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text("Oof, brilliant safe from the goalkeeper!\n", 0, 3)
                        slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
                        break
            else:
                slow_text("That is not a valid answer, please try again.\n", 0, 0)  
                continue

        # Penalty opponent
        slow_text("\nOpponents turn!\n", 0, 3)
        if chance_opponent == 1:
            team2_score += 1
            slow_text(f"{team2_name} manages to score the penalty!\n", 0, 3)
            slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
        else:
            team2_score += 0
            slow_text(f"{team2_name} misses the penalty!\n", 0, 3)
            slow_text(f"\nThe score is {team1_score} -- {team2_score}\n", 0, 3)
        
        return team1_score, team2_score


class MonsterFight:

    def enter_world(self):
        slow_text("You spot a cave in the distance.\n", 0, 3) 
        slow_text("You walk towards it and decide to enter it.\n", 0, 3)
        slow_text("As you slowly walk through the cave you approach a round door.\n", 0, 3)
        slow_text("It stops you from going further.\n", 0, 3)
        slow_text("There appears to be a riddle on the door:\n", 0, 3)
        slow_text("\tI am long\n", 0, 0)
        slow_text("\tI haven't got legs\n", 0, 0)
        slow_text("\tI can't walk\n", 0, 0)
        slow_text("\tI can slither\n", 0, 0)
        slow_text("\tI am green\n", 0, 1.5)
        slow_text("What am I?\n", 0, 0)

        attempts = 0
        while attempts < 3:
            guess = input("> ").lower()
            if guess == "snake":
                break
            else:
                attempts += 1
                print(f"Wrong. {3 - attempts} attempt(s) left.")
                continue
        else:
            slow_text("\nYou failed too many times.\n", 0, 2)
            slow_text("The environment starts shaking heavily.\n", 0, 3) 
            slow_text("The ceiling collapses on you.\n", 0, 3)
            slow_text("You're dead...", 0.3, 2)
            print("\n")
            return False

        slow_text("You hear a loud click. The door slowly opens...\n", 0 , 3)
        slow_text("In the distance you see a massive Basilisk sleeping on the floor...\n", 0, 4) 
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
                slow_text(f"You have {legend_hp}/500 HP\n\n", 0, 2)


class Main:

    def __init__(self):
        self.worlds = {
            'World 1': MonsterFight(), 
            'World 2': FootballFinal(),
            'World 3': GamesNight()
        }
        self.completed = {f'World {i}': False for i in range(1, 5)}

    def all_worlds_completed(self):
        if False in self.completed.values():
            return False
        else:
            return True

    def main_menu(self):
        print("\n--------")
        print("Welcome (back) to the main menu.\n")
        print("Available worlds:")
        print("\tWorld 1: Defeat a tough monster!")
        print("\tWorld 2: Champions League final!")
        print("\tWorld 3: Become a Game master!")
        print(f"\nCompleted: {', '.join([key for key, value in self.completed.items() if value is True])} \n")
        print("Type below the world you want to enter!")
        while True:
            world_choice = input("> ").lower()
            if world_choice not in map(lambda x: x.lower(), self.worlds.keys()):
                print("Not a world.")
                continue
            else:
                slow_text(f"Entering {world_choice.capitalize()}.\n", 0, 2)
                print("--------")
                break
        return world_choice.capitalize()
    
    def play(self):
        while True:
            world = self.main_menu()
            current_world_completed = self.worlds.get(world).enter_world()

            #ensures already completed world stays completed even if player restarts level and then loses the level
            if self.completed[world] is not True: 
                self.completed[world] = current_world_completed

            if self.all_worlds_completed():
                slow_text("Congratulations, you beat all worlds! Game ends now.", 0, 3)
                break


if __name__ == "__main__":
    game = Main()
    game.play()