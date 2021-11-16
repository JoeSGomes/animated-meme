from argparse import ArgumentParser
from random import randint

# GAMESWON = 0 
# GAMESATTEMPTED = 0 

# def play_jeopardy: 
#     if you win the gam: 
#         GAMESWON +=1
#         GAMESATTEMPTED += 1
#     elif you lose the game: 
#         GAMESATTEMPTED += 1
    

class HumanPlayer:
    """ This class will be used throughout the 3 games that will be played by the player. 
    """
    def __init__(self, name): 
        """This will contain the human player name. 

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
        value_dictionary = {}
        
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip()
                line_list = line_list.split(",")
                
                category = line_list[0]
                points = line_list[1]
                question = line_list[2]
                answer = line_list[3]

                value_dictionary[int(points)] = (question, answer)
                self.dictionary[category] = value_dictionary
                
    def available_questions(self, subject):
        """This method will be used to check which questions are available and from there, this will be displayed to the user.

    Args:
        subject (string): The subject is the type of question that can be choosen. For example, the subject here is pop culture, math, history. 

    Returns:
        [Str]: The list of available key left after the ones that have been said correspoinding the subject of the question. 
         """
        place = self.dictionary.get(subject)
        keys = place.keys()
        l = []
        for i in keys:
            l.append(i)
        return f'{subject} Questions Available: {l}'
                
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
        
        if subject[points] not in self.dictionary:
            raise KeyError ("question does not exist in the game!")
        else:
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


import sys
import time

class MemoryGame:
    """
    memory game where the player has to memorize 5 words
    Attributes:
        words(list): words to memorize
        t(int): time interval in seconds
    """
    def __init__(self, words, t):
        self.words = words
        self.t = t
    def display_words(self, index):
        """
        displays  five words for the player to memorize, separated by t sec intervals
        Args:
            index(int): location of the word we are referring to in words
        """
        print(self.word[index])
        time.sleep(self.t)
        print("/n")
        print("/n")
        print("/n")
        print("/n")
        print("/n")
        print("/n")
        print("/n")
    def questions(self, qs):
        """
        after each successful guess of a word, generates new question for player 
        to answer. 
        Args:
            qs(list): questions for player to answer
        """
        questions_tally = 3
        words_tally = 3
        while questions_tally != 0:
            qa1 = input("What is  the first element in the periodic table? ")
            if qa1 == "Hydrogen" or qa1 == "hydrogen":
                wa1 = input("What was the first word? ")
                if wa1 == self.words[0]:
                    print("Correct!")
                else:
                    words_tally = words_tally - 1
                    print(f"Incorrect you have {words_tally} chances left")
            else:
                questions_tally = questions_tally - 1
                print("Incorrect - answer was Hydrogen")
                print(f"You have {questions_tally} left")
                
            qa2 = input("What is 6/(2(1+2))?")
            if qa2 == 1:
                wa2 = input("What was the second word? ")
                if wa2 == self.words[1]:
                    print("Correct!")
                else:
                    words_tally = words_tally - 1
                    print(f"Incorrect you have {words_tally} chances left")
            else:
                questions_tally = questions_tally - 1
                print("Incorrect - answer was 1")
                print(f"You have {questions_tally} left")
                
            qa3 = input("Who was the second president of the United States? ")
            if qa3 == "John Adams" or qa3 == "john adams":
                wa3 = input("What was the third word? ")
                if wa3 == self.words[2]:
                    print("Correct!")
                else:
                    words_tally = words_tally - 1
                    print(f"Incorrect you have {words_tally} chances left")
            else:
                questions_tally = questions_tally - 1
                print("Incorrect - answer was John Adams")
                print(f"You have {questions_tally} left")
            
            qa4 = input("What shape is generally used for stop signs? ")
            if qa4 == "Octagon" or qa4 == "octagon":
                wa4 = input("What was the fourth word? ")
                if wa4 == self.words[3]:
                    print("Correct!")
                else:
                    words_tally = words_tally - 1
                    print(f"Incorrect you have {words_tally} chances left")
            else:
                questions_tally = questions_tally - 1
                print("Incorrect - answer was an octagon")
                print(f"You have {questions_tally} left")
                
            qa5 = input("How many continents are there on Earth? ")
            if qa5 == 7 or qa5 == "Seven" or qa5 == "seven":
                wa5 = input("What was the fifth word? ")
                if wa5 == self.words[4]:
                    print("Correct!")
                else:
                    words_tally = words_tally - 1
                    print(f"Incorrect you have {words_tally} chances left")
            else:
                questions_tally = questions_tally - 1
                print("Incorrect - answer was 7")
                print(f"You have {questions_tally} left")      
                
words = "apple", "orange", "banana", "tomato", "grape"
interval = 2
mg = MemoryGame(words, interval)
   
  
class GuessNumber:   
    """
    Class that contains all the logic related to the "Guess the number" game

    Attributes:
        tries (int): number of allowed tries
        hints (int): number of hints that the player can use
    """
    def __init__(self, tries = 10, hints = 3):
        self.tries = tries
        self.hints = hints

    def mechanics_of_game(self, lower_bound = 1, upper_bound = 50):
        """
        This method handles the logic of the game

        Args:
            lower_bound (int): the lower bound of the target integer. Defaults to 1
            upper_bound (int): the upper bound of the target integer. Defaults to 50

        Side effects:
            Prints the game state and input prompts to the standard output
            Prints the result of the game
        """
        target_number = randint(lower_bound, upper_bound)
        print("The number you are looking for is between {} and {}".format(lower_bound, upper_bound))
        correctly_guessed = False
        for i in range(self.tries):
            guess = int(input("Make a guess: "))
            if guess == target_number:
                correctly_guessed = True
                break
            else:
                print("Incorrect guess!")
            
        if correctly_guessed:
            print("Correct guess! You won!")
        else:
            print("You ran out of tries; better luck next time!")
    
    def hints(counter, number): 
        '''
        this method gives 3 separate hints for player if requested
        
        Args: 
            counter(int): counter starts at 0, each time player prompts 'hint' 1 is added to counter to
                          total 3 at the end.
            number(int): the random number generated, will be added or subtracted or added by hint
        
        '''
	
        if counter ==  1: 
            print (f"Number is between {number - 20} and {number + 20}")
        
        elif counter == 2:
            print (f"Number is between {number - 10} and {number + 10}")
        
        elif counter == 3:
            print (f"Number is between {number - 5} and {number + 5}")
        
        else:
            print(f"You already used your guesses. Reminder number is between {number - 5} and 	{number + 5}")


# def main (): 
#     games_won = 0 
#     games_attempted = 0 
    
#     while games_won < 3 and games_attempted <= 3:
#         choice = input("What game do you want to play? ")
#         if choice == "Jeopardy": 
#             game = Jeopardy()
#             game.play_jeopardy()
#             games_attempted += 1 
            
#         elif choice == "Memory Game": 
#             game = MemoryGame()
#             game.play_memory_game()
#             games_attempted += 1 
        
#         elif choice == "Guess the Number": 
#             game = GuessNumber()
#             game.play_guess_number()
#             games_attempted += 1 
        
#         else: 
#             raise ValueError ("Sorry, that is not a valid game, try again!")


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