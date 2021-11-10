class HumanPlayer:
    
    
    
class Jeopardy:
        
    

class JeopardyCatalog:
    def __init__(self, file):
        self.list = []
        history = {}
        pop_culture = {}
        math = {}
        
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                line_list = line.strip()
                line_list = line_list.split(",")
                
                category = line_list[0]
                points = line_list[1]
                question = line_list[2]
                answer = line_list[3]
                if category[0] == "History":
                    history[points] = (question, answer)
                    self.list.append(history)
                elif category[0] == "Pop Culture":
                    pop_culture[points] = (question, answer)
                    self.list.append(pop_culture)
                elif category[0] == "Math":
                    math[points] = (question, answer)
                    self.list.append(math)
                
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
            dictionary = self.list.get(subject)
            
            question_answer_pair = dictionary[points]
            question = question_answer_pair[0]
            
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
            
        question_answer_pair = dictionary[points]
        answer = question_answer_pair[1]
            
        return answer  
    

class MemoryGame:
