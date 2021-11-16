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
         

def main(filename):
    catalog = JeopardyCatalog(filename)
    
    print()
    print("Dictionary in Easy Access Format: \n")
    print(catalog.dictionary)



main("jeopardy.txt")