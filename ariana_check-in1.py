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
        print(self.words[0])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        print(self.words[1])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        print(self.words[2])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        print(self.words[3])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        print(self.words[4])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
    def questions(self):
        """
        after each successful guess of a word, generates new question for player 
        to answer. 
        """
        questions_tally = 3
        words_tally = 3
        while questions_tally != 0:
            qa1 = input("What is  the first element in the periodic table? ")
            if qa1.lower() == "Hydrogen":
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
            if qa2 == 1 or qa2.lower() == "One":
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
            if qa3.lower() == "john adams":
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
            if qa4.lower() == "Octagon":
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
            if qa5 == 7 or qa5.lower() == "Seven":
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
print(mg.display_words(interval))
print(mg.questions())
