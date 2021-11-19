class HumanPlayer:
    """ This class will be used throughout the 3 games that will be played by the player. 
    """
    def __init__(self, name, games_won, games_attemped): 
        """This will contain the human player name. 

        Args:
            name (Str): The name of the human that will be playing the game. 
        """
        self.name = name 
        self.games_won = games_won
        self.games_attemped = games_attemped

    
    
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
        while self.current_points < 3000 and JeopardyCatalog.total_game_available_points(self) > 0:
            JeopardyCatalog.available_questions("Math")
            JeopardyCatalog.available_questions("History")
            JeopardyCatalog.available_questions("Pop Culture")
            
            user_subject = input("Which subject do you want to attempt? ").strip()
            
            while user_subject != "Math" or user_subject != "History" or user_subject != "Pop Culture": 
                print("Sorry, that is not a valid subject, please try again!")
                user_subject = input("Which subject do you want to attempt? ").strip()
                
            if user_subject == "Math" or user_subject == "History" or user_subject == "Pop Culture":
                user_points = input("How many points do you want to attempt? ").strip()
            points_available = JeopardyCatalog.available_points(user_subject)
            
            while user_points not in points_available:
                print("Sorry that question does not exists, try again. ")
                user_points = input("How many points do you want to attempt? ").strip()
                points_available = JeopardyCatalog.available_points(user_subject)
                
            if user_points in points_available:
                user_answer = input(JeopardyCatalog.get_question(user_subject, user_points))
                
                if user_answer == JeopardyCatalog.get_answer(user_subject, user_points):
                    print( f'That was correct! You got {JeopardyCatalog.get_points(user_points)} points')
                    self.current_points += self.get_points(user_points)
                    JeopardyCatalog.update_dictionary(user_subject, user_points)
                else: 
                    print("That was incorrect! ")
                    JeopardyCatalog.update_dictionary(user_subject, user_points)
        if self.current_points >= 3000 and JeopardyCatalog.total_game_available_points(self) > 0: 
            HumanPlayer.games_won == 1
            
        HumanPlayer.games_attempted += 1
        
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
        return f'{subject} Questions Available: {l}'
    
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
        
        history_points = self.dictionary.get("History")
        points = history_points.keys()
        for i in int(points):
            total_points += i
            
        math_points = self.dictionary.get("Math")
        points_m = math_points.keys()
        for i in int(points_m):
            total_points += i
            
        pop_culture_points = self.dictionary.get("Pop Culture")
        points_pc = pop_culture_points.keys()
        for i in int(points_pc):
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
        

HumanPlayer("Kishan", 0, 0)
print(JeopardyCatalog("jeopardy.txt"))
game = Jeopardy(0)
print(game.play_jeopardy_game())
