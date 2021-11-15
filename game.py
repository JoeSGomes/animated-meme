from argparse import ArgumentParser

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
                
                if category == "Pop Culture":
                    pop_culture[int(points)] = (question, answer)
                elif category == "History":
                    history[int(points)] = (question, answer)
                elif category == "Math":
                    math[int(points)] = (question, answer)
                    
            self.dictionary["Pop Culture"] = pop_culture
            self.dictionary["Math"] = math
            self.dictionary["History"] = history
         
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
        
        
        #return question
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
    
    def get_points(self, subject, points):
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
        del self.dictionary[subject][points]
        
        return int(points)



    
class MemoryGame:

  
class GuessNumber:   



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
