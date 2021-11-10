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
                
                
    
    

class MemoryGame:
