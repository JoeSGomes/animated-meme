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
        
    

class JeopardyCatalog:
    def __init__(self, file):
        self.dictionary = {}
        
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip()
                line_list = line_list.split(",")
                
                category = line_list[0]
                points = line_list[1]
                question = line_list[2]
                answer = line_list[3]

                self.dictionary[category + points] = (int(points), question, answer)
                
    def get_question(self, subject, points):
        """
        gets the question from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
        
        Returns:
            the cooresponding question the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        
        key = subject + str(points)
        
        if key not in self.dictionary:
            raise KeyError ("subject does not exist in the game!")
        else:
            dictionary = self.dictionary.get(subject + str(points))
            question = dictionary[1]
            del self.dictionary[subject + points]
            
            return question        
    
    def get_answer(self, subject, points):
        """
        gets the answer from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
        
        Returns:
            the cooresponding answer the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        key = subject + str(points)
        dictionary = self.dictionary.get(key)            
        answer = dictionary[2]
            
        return answer  
    
    def get_points(self, subject, points):
        """
        gets the points from the catalog that is named
        Args:
            subject (string): the topic of the user has chosen to answer
        
        Returns:
            the cooresponding points for the question the user has requested
        
        Raises:
            KeyError: if the name of the subject is not in the catalog
        """
        
        key = subject + str(points)        
        dictionary = self.dictionary.get(key)            
        points = dictionary[0]
            
        return points  

class MemoryGame:
