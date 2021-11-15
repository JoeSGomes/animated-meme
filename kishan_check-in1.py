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

def main(filename):
    catalog = JeopardyCatalog(filename)
    
    print()
    print("Origional Dictionary: \n")
    print(catalog.dictionary)
    print("\n\n")

    question = catalog.get_question("Pop Culture", 500)
    print("Question:", question)
    
    answer = catalog.get_answer("Pop Culture", 500)
    print("Answer:", answer) 
    
    points = catalog.get_points("Pop Culture", 500)
    print("Points:", points)
    
    print("\n\n")

    print("New Dictionary: With Question Removed\n")
    print(catalog.dictionary)
    print("\n\n")


main("jeopardy.txt")