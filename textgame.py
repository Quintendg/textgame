from random import randint
import time


def slow_text(string, delay, wait):
    """ Print string letter after letter instead of at once. """

    for char in string:
        print(char, end='')
        time.sleep(delay)
    time.sleep(wait)

        
class FootballFinal:

    def __init__(self):
        self.team1_scores = 0
        self.team2_scores = 0

    def enter_world(self):
        slow_text("Reporter:\n", 0, 2)
        slow_text("Welcome to the final of the Champions League on this beautiful day!\n", 0, 3)
        slow_text("Today, the two teams will battle for eternal glory.\n", 0, 3)
        slow_text("The match ended in 2-2 in the regular time.\n", 0, 2)
        slow_text("Now, penalties are needed to decide who will be the winner!\n", 0, 3)
        slow_text("The first team to take a penalty is:\n", 0, 2)
        
        print("\nChoose your favourite player: (please enter the number of the player)")
        print("1: \tLionel Messi")
        print("2: \tCristiano Ronaldo")
        print("3: \tRobert Lewandowski")
        print("4: \tGeorginio Wijnaldum")
        print("5: \tKevin de Bruyne")
        
        # Choosing team
        while True:
            team1 = input("> ")
            if team1 == "1":
                team1_name = "Barcelona"
                print("Your team is Barcelona!")
                break
            elif team1 == "2":
                team1_name = "Juventus"
                print("Your team is Juventus!")
                break
            elif team1 == "3":
                team1_name = "Bayern München"
                print("Your team is Bayern München!")
                break
            elif team1 == "4":
                team1_name = "Liverpool"
                print("Your team is Liverpool!")
                break
            elif team1 == "5":
                team1_name = "Manchester City"
                print("Your team is Manchester City!")
                break
            else:
                print("Please enter a valid number.")
                continue
        
        slow_text("\nAnd on the other side of the field we have:\n", 0, 1)
         
        print("\nChoose another player: (please enter the number of the player)")
        print("1: \tLionel Messi")
        print("2: \tCristiano Ronaldo")
        print("3: \tRobert Lewandowski")
        print("4: \tGeorginio Wijnaldum")
        print("5: \tKevin de Bruyne")
        
        # Choosing opponents team
        while True: 
            team2 = input("> ")
            if team2 != team1:
                if team2 == "1":
                    team2_name = "Barcelona"
                    print("The other team is Barcelona!")
                    break
                elif team2 == "2":
                    team2_name = "Juventus"
                    print("The other team is Juventus!")
                    break
                elif team2 == "3":
                    team2_name = "Bayern München"
                    print("The other team is Bayern München!")
                    break
                elif team2 == "4":
                    team2_name = "Liverpool"
                    print("The other team is Liverpool!")
                    break
                elif team2 == "5":
                    team2_name = "Manchester City"
                    print("The other team is Manchester City!")
                    break
                else:
                    print("Please enter a valid number.")
                    continue
            elif team2 == team1:
                print("You have already chosen this team!\nPlease choose another team.")
                continue
        
        slow_text(f"\nSo, can {team1_name} handle the pressure better than {team2_name}?\n", 0, 3)
        print("-"*10)
        
        # Players need to answer questions correct to have a higher chance to score a penalty
        slow_text("Answer questions correct to have a higher chance to score a penalty.\n", 0, 3)
        slow_text("The team which manages to score the most penalties is the winner!\n", 0, 3)
        slow_text("All answers are 'True' or 'False'.\n", 0, 3)
        
        # Question 1, true is correct
        question1 = "\nQuestion 1:\n\nCOVID-19 is an abbreviation for Corona Virus Disease 2019"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question1, question_outcome)
    
        # Question 2, false is correct
        question2 = "\nQuestion 2:\n\nM&M stands for Mars and Moordale"
        question_outcome = "False"
        self.scores_question(team1_name, team2_name, question2, question_outcome)

        # Question 3, false is correct
        question3 = "\nQuestion 3:\n\nThere are two parts of the body that can't heal themselves"
        question_outcome = "False"
        self.scores_question(team1_name, team2_name, question3, question_outcome)
        
        # Question 4, true
        question4 = "\nQuestion 4:\n\nBananas are curved because they grow upwards towards the sun"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question4, question_outcome)
        
        # Question 5, true
        question5 = "Question 5:\n\nIn the 'normal' Harry Potter story, there are 7 books and 8 movies\n"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question5, question_outcome)            
        
        # Question 6, true
        question6 = "\nQuestion 6:\n\nThe small intestine is about 7 meters long\n"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question6, question_outcome)
        
        # Question 7, false
        question7 = "\nQuestion 7:\n\nCoffee will dehydrate you\n"
        question_outcome = "False"
        self.scores_question(team1_name, team2_name, question7, question_outcome)
        
        # Question 8, false
        question8 = "\nQuestion 8:\n\nSydney is the capital of Australia\n"
        question_outcome = "False"
        self.scores_question(team1_name, team2_name, question8, question_outcome)
        
        # Question 9, true
        question9 = "\nQuestion 9:\n\nCarrots are good for your eyes\n"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question9, question_outcome)
        
        # Question 10, false
        question10 = "\nQuestion 10:\n\nLightning never strikes the same place twice\n"
        question_outcome = "False"
        self.scores_question(team1_name, team2_name, question10, question_outcome)
        
        # Question 11, true
        question11 = "\nQuestion 11:\n\nPeople in Japan eat Kentucky Fried Chicken for Christmas dinner\n"
        question_outcome = "True"
        self.scores_question(team1_name, team2_name, question11, question_outcome)

        if self.team1_scores > self.team2_scores:
            slow_text(f"Congratulations, {team1_name} wins the Champions League after penalties!!!\n", 0, 5)
            return True
        else:
            slow_text(f"You lost! {team2_name} wins the Champions League after penalties...\n", 0, 5)
            return False
            

    def scores_question(self, team1_name, team2_name, question, question_outcome):
        """ Gives a score to a team depending on correct answering of a question. 
        Gives also a score for the opponents team"""
    
        question_right = randint(1, 10)
        question_wrong = randint(1, 6) #chance to score a penalty when question is wrong
        chance_opponent = randint(1, 2) #chance for the opponent to score
        true = ["True", "true", "T", "t"]
        false = ["False", "false", "F", "f"]
        
        print(question)
        while True:
            choice = input("> ")
            if question_outcome == "True": #answer is true
                if choice in false:
                    if question_wrong < 2:
                        self.team1_scores += 1
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text(f"However, {team1_name} manages to score a really lucky goal!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                    else:
                        self.team1_scores += 0
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text("Oof, brilliant safe from the goalkeeper!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                elif choice in true:
                    if question_right <= 8:
                        self.team1_scores += 1
                        slow_text("Correct!\n", 0, 2)
                        slow_text(f"{team1_name} manages to score the penalty!!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                    else:
                        self.team1_scores += 0
                        slow_text("Correct!\n", 0, 2)
                        slow_text("Auch, that is an unlucky shot! He misses..\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                else:
                    slow_text("That is not a valid answer, please try again.\n", 0, 3)  
                    continue
            elif question_outcome == "False": #answer is false
                if choice in true:
                    if question_wrong < 2:
                        self.team1_scores += 1
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text(f"However, {team1_name} manages to score a really lucky goal!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                    else:
                        self.team1_scores += 0
                        slow_text("Wrong answer!\n", 0, 2)
                        slow_text("Oof, brilliant safe from the goalkeeper!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                elif choice in false:
                    if question_right <= 8:
                        self.team1_scores += 1
                        slow_text("Correct!\n", 0, 2)
                        slow_text(f"{team1_name} manages to score the penalty!!\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                    else:
                        self.team1_scores += 0
                        slow_text("Correct!\n", 0, 2)
                        slow_text("Auch, that is an unlucky shot! He misses..\n", 0, 3)
                        slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
                        break
                else:
                    slow_text("That is not a valid answer, please try again.\n", 0, 0)
                    continue

            # Penalty opponent
        slow_text("\nOpponents turn!\n", 0, 3)
        if chance_opponent == 1:
            self.team2_scores += 1
            slow_text(f"{team2_name} manages to score the penalty!\n", 0, 3)
            slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)
        else:
            self.team2_scores += 0
            slow_text(f"{team2_name} misses the penalty!\n", 0, 3)
            slow_text(f"\nThe score is {self.team1_scores} -- {self.team2_scores}\n", 0, 3)


class MonsterFight:

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
            'World 1': MonsterFight(), 
            'World 2': FootballFinal(),
            # 'World 3': ,
            # 'World 4': 
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
        print("\tWorld 2: Champions League final!\n")
        print(f"Completed: {', '.join([key for key, value in self.completed.items() if value is True])} \n")
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
            if self.completed[world] is not True: #assures already completed world stays completed even if player restarts level and then loses the level
                self.completed[world] = current_world_completed
            if self.all_worlds_completed():
                slow_text("Congratulations, you beat all worlds! Game ends now.", 0, 3)
                break


if __name__ == "__main__":
    game = Main()
    game.play()