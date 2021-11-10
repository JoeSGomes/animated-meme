class HumanPlayer:
    
    
    
class Jeopardy:
        
    

class JeopardyCatalog:
    def __init__(self, file):
        self.dictionary = {}
        
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip()
                line_list = line_list.split(",")
                
                category = line_list[0]
                descrip_points = line_list[1]
                points = int(line_list[1])
                question = line_list[2]
                answer = line_list[3]

                self.dictionary[category + descrip_points] = (points, question, answer)
                
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
        if subject not in self.list:
            raise KeyError ("subject does not exist in the game!")
        else:
            dictionary = self.dictionary.get(subject + points)
            
            question = dictionary[1]
            
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
        
        dictionary = self.list.get(subject)
            
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
        
        dictionary = self.list.get(subject)
            
        points = dictionary[0]
            
        return points  

class MemoryGame:
