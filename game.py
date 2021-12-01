from argparse import ArgumentParser
import random
import time
import sys

GAMES_WON = 0
GAMES_ATTEMPTED = 0

class HumanPlayer:
    """ This class will be used throughout the 3 games that will be played by the player. 
    """
    def __init__(self, name): 
        """This will contain the human player name. 
       
        Attributes:
        name(str): This will be the player name that will be playing the games. 
            
        Args:
            name (Str): The name of the human that will be playing the game. 
        """
        self.name = name 

class Jeopardy:
    """This class is run the jeopardy game the player has selected. 
    """
    def __init__(self, current_points):
        """This fucntion will hold the current point status of the jeoparty game. 
        
        Args:
            current_points (int): THe current point of the human player. 
        """
        self.current_points = current_points
    
    def play_jeopardy_game(self):
        global GAMES_WON
        catalog = JeopardyCatalog("jeopardy.txt")

        quit = 0
        
        while self.current_points < 3000 and (self.current_points + catalog.total_game_available_points()) >= 3000 and quit != 1:  
            print()
            print(f'history questions available: {catalog.available_questions("history")}')
            print(f'math questions available: {catalog.available_questions("math")}')
            print(f'pop culture questions available: {catalog.available_questions("pop culture")}')
            
            print(f'\nYou currently have acquired {self.current_points}/3,000 points so far to win the game\n')

            math = "math"
            history = "history"
            pop_culture = "pop culture"
            
            user_subject = input("Which subject do you want to attempt? ").lower().strip()
            
            while not ((user_subject == math or user_subject == history or user_subject == pop_culture) and len(catalog.available_questions(user_subject))):
                print()
                print("\nSorry, that is not a valid subject, please try again!\n\n")
                
                print(f'history questions available: {catalog.available_questions("history")}')
                print(f'math questions available: {catalog.available_questions("math")}')
                print(f'pop culture questions available: {catalog.available_questions("pop culture")}')
                
                print(f'\nYou currently have acquired {self.current_points}/3,000 points so far to win the game\n')
                
                user_subject = input("Which subject do you want to attempt? ").lower().strip()
                
            if user_subject == math or user_subject == history or user_subject == pop_culture:
                check = 0
                while check != 1:
                    user_points = (input("How many points do you want to attempt? ").strip())
                    check = user_points.isnumeric()
                    if check == 1:
                        user_points = int(user_points)
                        break
                    print("\nSorry that is a invalid input, try again.\n\n")
                    
                    print(f'history questions available: {catalog.available_questions("history")}')
                    print(f'math questions available: {catalog.available_questions("math")}')
                    print(f'pop culture questions available: {catalog.available_questions("pop culture")}')
                    print(f'\nYou currently have acquired {self.current_points}/3,000 points so far to win the game\n')
                
            points_available = catalog.available_points(user_subject)
            
            while user_points not in points_available:
                print("\nSorry that question does not exists, try again.\n\n")
                check = 0
                while check != 1 and user_points not in points_available:
                    print(f'history questions available: {catalog.available_questions("history")}')
                    print(f'math questions available: {catalog.available_questions("math")}')
                    print(f'pop culture questions available: {catalog.available_questions("pop culture")}')
                    print(f'\nYou currently have acquired {self.current_points}/3,000 points so far to win the game\n')
                    user_points = (input("How many points do you want to attempt? ").strip())
                    check = user_points.isnumeric()
                    if check == 1:
                        user_points = int(user_points)
                        break
                    print("\nSorry that question does not exists, try again.\n\n")
                    
                points_available = catalog.available_points(user_subject)
                
            if user_points in points_available:
                user_answer = input(catalog.get_question(user_subject, user_points)).lower().strip()
                
                if user_answer == catalog.get_answer(user_subject, user_points):
                    print( f'\nThat was correct! You got {catalog.get_points(user_points)} points\n')
                    self.current_points += catalog.get_points(user_points)
                    catalog.update_dictionary(user_subject, user_points)
                else: 
                    print("\n\nThat was incorrect! Better luck on the next question...\n")
                    catalog.update_dictionary(user_subject, user_points)
                    
        if self.current_points >= 3000: 
            print("Congrats! You won the game. Good luck with your next one...")
            GAMES_WON += 1 
        else:
            print("Sorry, you ran out of opportunities, better luck next game!")
            print(f'\nYou ended the game with {self.current_points}/3,000 points\n')        
        
        x = ""
        return x

class JeopardyCatalog:
    """
    This class extracts the text file used for the jeopardy game and converts it to extract wanted values
    
    Attributes:
        dictionary (dict): a dictionary of all of questions and the associated answers, points, and subjects
    """
    def __init__(self, file):
        """
        initializes the object and converts the text file to the desired dictionary
        
        Args:
        file (file): the text file that will be used for converting to a dictionary
        
        Side effects:
        adding values to the dictionary attribute
        """
        self.dictionary = {}
        pop_culture = {}
        history = {}
        math = {}
        
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip()
                line_list = line_list.split(",")
                
                category = line_list[0]
                points = line_list[1]
                question = line_list[2]
                answer = line_list[3]
                
                if category == "pop culture":
                    pop_culture[int(points)] = (question, answer)
                elif category == "history":
                    history[int(points)] = (question, answer)
                elif category == "math":
                    math[int(points)] = (question, answer)
                    
            self.dictionary["pop culture"] = pop_culture
            self.dictionary["math"] = math
            self.dictionary["history"] = history
            
                
    def available_questions(self, subject):
        """This method will be used to check which questions are available and from the dictionary, this will be displayed to the user.

        Args:
        subject (string): The subject is the type of question that can be choosen. 

        Returns:
        [Str]: The list of available key left after the ones that have been said correspoinding the subject of the question. 
         """
        place = self.dictionary.get(subject)
        keys = place.keys()
        l = []
        for i in keys:
            l.append(int(i))
        return l
    
    def available_points(self, subject):
        """This method will be used to check which questions are available and from the dictionary, this will be displayed to the user.

        Args:
        subject (string): The subject is the type of question that can be choosen. 

        Returns:
        [Str]: The list of available key left after the ones that have been said correspoinding the subject of the question. 
         """
        place = self.dictionary.get(subject)
        keys = place.keys()
        l = []
        for i in keys:
            l.append(i)
        return l
    
    def total_game_available_points(self):
        total_points = 0
        
        history_points = self.dictionary.get("history")
        points = history_points.keys()
        for i in points:
            total_points += i
            
        math_points = self.dictionary.get("math")
        points_m = math_points.keys()
        for i in points_m:
            total_points += i
            
        pop_culture_points = self.dictionary.get("pop culture")
        points_pc = pop_culture_points.keys()
        for i in points_pc:
            total_points += i
            
        return total_points
                
    def get_question(self, subject, points):
        """
        gets the question from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
            points(int): the amount of points for the question that the user has chosen to answer
        
        Returns:
            the cooresponding question the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        

        question = self.dictionary[subject][points][0]

        return question        
    
    def get_answer(self, subject, points):
        """
        gets the answer from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
            points(int): the amount of points for the question that the user has chosen to answer
            
        Returns:
            the cooresponding answer the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        answer = self.dictionary[subject][points][1]
            
        return answer  
    
    def get_points(self, points):
        """
        gets the points from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
            points(int): the amount of points for the question that the user has chosen to answer
            
        Returns:
            the cooresponding points for the question the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        
        return points
    
    def update_dictionary(self, subject, points):
        """
        updates the dictionary by deleting the question the user chose
        
        Args:
            subject (string): the topic of the user has chosen to answer
            points(int): the amount of points for the question that the user has chosen to answer

        Side effects:
            deleting keys and values from the dictionary attribute
        """
        del self.dictionary[subject][points]
        

class MemoryGame:
    """
    memory game where the player has to memorize 5 words
    Attributes:
        words(list): words to memorize
        t(int): time interval in seconds
    """
    def __init__(self,time, questions_tally = 3, words_tally = 3):
        self.words = ["apple", "pencil", "isolation", "broccoli", "pterodactyl"]
        self.time = time
        self.questions_tally = questions_tally
        self.words_tally = words_tally
    def display_words(self, index):
        """
        displays  five words for the player to memorize, separated by t sec intervals
        Args:
            index(int): location of the word we are referring to in words
        """
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        time.sleep(self.time)
        print("Get Ready!")
        print("\n")
        print("\n")
        time.sleep(.5)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print(self.words[index])
        print("\n")
        print("\n")
        time.sleep(self.time)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        x = ""
        return x
        
    def questions(self, index, question, question_answer):
        """
        allows user to answer five questions to throw them off reciting the words from memory
        Args:
            i(int): index for word in words
            q(string): question for the user to answer
            a(string): correct answer
        """

        word_answer = self.words[index]
        word_user_answer = ""

        print(f'Reminder: You have {self.questions_tally} tries left to guess the question answer\n')
        user_answer = input(question).strip()

        while user_answer.lower() != question_answer:
            if user_answer.lower() != question_answer and self.questions_tally != 1:
                self.questions_tally -= 1
                print("\nSorry, that was incorrect, please try again!")
                print(f'\nYou have {self.questions_tally} tries left to guess the question answer\n')
                user_answer = input(question).strip()
                
            else:
                self.questions_tally -= 1
                break

        if user_answer.lower() == question_answer:
            print("\nCorrect, now onto guessing the word...")
            print(f'\nReminder: You have {self.words_tally} tries left to guess the word\n')
            
            word_user_answer = input("What was the word? ").strip()
            
            while word_user_answer.lower() != word_answer and self.words_tally != 1:
                self.words_tally -= 1
                print("Sorry, that was incorrect, please try again!\n")
                print(f'You have {self.words_tally} tries left to guess the word\n')
                word_user_answer = input("What was the word? ").strip()
        
            if word_user_answer.lower() == word_answer:
                print("\nYou got it right, onto the next challenge!")
                time.sleep(self.time) 
                    
        if word_user_answer != word_answer:
            self.words_tally -= 1     
                  
        if self.questions_tally < 1 or self.words_tally < 1:
            print("\nSorry, that was incorrect, and you ran out of tries!\n")
            print("\nYou lost. Better luck next time!")        
        
        x = ""  
        return x  

    def mechanics(self):
        global GAMES_WON
        dictionary_questions = {1 : "What is the first element in the periodic table? ",
                                2 : "What is the last letter of the alphabet? ",
                                3 : "Who was the second president of the United States? ",
                                4 : "What shape is generally used for stop signs? ",
                                5 : "Who won the 2021 World Series? "}
        questions_key = 1
        
        dictionary_answers = {1 :"hydrogen",
                            2 : "z",
                            3 : "john adams",
                            4 : "octagon",
                            5 : "braves"}
        answer_key = 1
        
        index = 0
        
        while self.questions_tally > 0 and self.words_tally > 0 and index <= 4:
            self.display_words(int(index))
            self.questions(int(index), dictionary_questions[questions_key], dictionary_answers[answer_key])
            questions_key += 1
            answer_key += 1
            index += 1
        
        if self.questions_tally > 0 and self.words_tally > 0 and index > 4:
            print("\nCongratulations! The game is over and you won! Good luck with your other games!\n")
            GAMES_WON += 1
            
        x = ""
        return x

class GuessTheNumber:
    """
    Class that contains all the logic related to the "Guess the number" game

    Attributes:
        tries (int): number of allowed tries
        hints (int): number of hints that the player can use
    """
    def __init__(self, tries = 10, hints_left = 3):
        self.tries = tries
        self.hints_left = hints_left

    def hints(self, target_number):
        """
        This method handles providing hints to the user

        Args:
            target_number (int): the target number of the game (i.e. the number that the
                user is trying to guess)

        Side effects:
            Prints a hint to the standard output
            Updates the number of hints left
        """
        
        if self.hints_left ==  3:
            upper = target_number + 20
            lower = target_number - 20 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
                
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
        
        elif self.hints_left == 2:
            upper = target_number + 10
            lower = target_number - 10 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
            
        
        elif self.hints_left == 1:
            upper = target_number + 5
            lower = target_number - 5 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
        
        else:
            upper = target_number + 5
            lower = target_number - 5 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print(f"You already used your guesses. Reminder number is between {lower} and {upper}")
            
    def mechanics_of_game(self, lower_bound = 1, upper_bound = 50):
        global GAMES_WON
        """
        This method handles the logic of the game

        Args:
            lower_bound (int): the lower bound of the target integer. Defaults to 1
            upper_bound (int): the upper bound of the target integer. Defaults to 50

        Side effects:
            Prints the game state and input prompts to the standard output
            Prints the result of the game
        """
        target_number = random.randint(lower_bound, upper_bound)
        print("The number you are looking for is between {} and {}".format(lower_bound, upper_bound))
        correctly_guessed = False
        target_number = random.randint(lower_bound, upper_bound)
        print("The number you are looking for is between {} and {}".format(lower_bound, upper_bound))
        correctly_guessed = False
        i = 0
        while i < self.tries:
            user_input = input("Make a guess (or type 'H' to get a hint): ")
            if user_input == 'H':
                self.hints(target_number)
            elif user_input.isnumeric():
                guess = int(user_input)
                if guess == target_number:
                    correctly_guessed = True
                    break
                else:
                    print("Incorrect guess!")
            else:
                print("Wrong input!")
                continue
            i += 1
            
        if correctly_guessed:
            print("Correct guess! You won!")
        else:
            print("You ran out of tries; better luck next time!")
            
def play_games(filename):
    global GAMES_ATTEMPTED
    global GAMES_WON
    
    games =['memory game', 'jeopardy', 'guess the number']
    
    player_name = input("What is your name? ")
    player = HumanPlayer(player_name)
    
    while GAMES_WON < 2 and GAMES_ATTEMPTED <= 3:  
        if GAMES_WON < 2 and len(games) == 1:
            print("Sorry, you have run out of attempts to play. Better luck next time")
            break
        else:
            print(f'\nYou have won {GAMES_WON} games and attempted {GAMES_ATTEMPTED} games')
            choice = input(f'\n\n {player.name}, which game would you like to play? \n {games}: ').strip().lower()
        
            while choice not in games:
                print("Sorry, that game does not exist. Please try again!")
                print(f'\nYou have won {GAMES_WON} games and attempted {GAMES_ATTEMPTED} games')
                choice = input(f'\n\n {player.name}, which game would you like to play? \n {games}: ').strip().lower()
        
            if choice == "jeopardy": 
                jg = Jeopardy(0)
                JeopardyCatalog(filename)
                print(jg.play_jeopardy_game())
                games.remove('jeopardy')
                GAMES_ATTEMPTED += 1 
            
            elif choice == "memory game": 
                mg = MemoryGame(.5)
                print(mg.mechanics())
                games.remove("memory game")
                GAMES_ATTEMPTED += 1
            
            elif choice == "guess the number": 
                gg = GuessTheNumber()
                GAMES_ATTEMPTED += 1
                games.remove('guess the number')
                print(gg.mechanics_of_game())

    if GAMES_WON == 2 and GAMES_ATTEMPTED <= 3:
        print(f"Congrats {player.name}! You have successfully won this game!")
        print(f'You have won {GAMES_WON} games and attempted {GAMES_ATTEMPTED} games')
    else:
        print(f"Sorry {player.name}, you ran out of tries and you have lost the game. Please try again next time")
        print(f'You have won {GAMES_WON} games and attempted {GAMES_ATTEMPTED} games')
    
    x = ""
    
    return x
        
def main(filename):
    play_games(filename)

        
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
    - filename: a path to a CSV file containing Jeapordy Game's questions, points, and answers
    
        Args:
arglist (list of str): arguments from the command line.
    
    Returns:
    namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="path to CSV file containing questions, points, and answers to the Jeapordy Game")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)

"""
Methods Distribution:

Kishan (3): __init()__ for jeopardy catalog, total_game_available_points(), available_points() --> JeopardyCatalog Class
Walter (2): hints() --> GuessTheNumber Class, play_games() method
Joe (2): available_questions() --> JeopardyCatalog Class, play_jeopardy_game() --> Jeopardy Class
Ariana (2): questions(), mechanics() --> MemoryGame Class
Naila (2): mechanics_of_game() --> GuessTheNumber Class, parse_args() method
"""