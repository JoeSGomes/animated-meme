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
        print(self.words[index])
        time.sleep(self.t)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
    def question1(self):
      questions_tally = 3
      words_tally = 3
      qa1 = input("What is the first element in the periodice table? ")
      if questions_tally <= 0 or words_tally <= 0:
        print("Game Over.")
        while qa1.lower() != "hydrogen":
            questions_tally -= 1
            qa1 = input("What is the first element in the periodice table? ")

        if qa1.lower() == "hydrogen":
            wa1 = input("What was the first word? ")
            while wa1.lower() != self.words[0]:
                words_tally -= 1
                print("Sorry, that was incorrect, please try again!")
                print(f'You have {words_tally} questions left')
                wa1 = input("What was the first word? ")
                
      if wa1.lower() == self.words[0]:
          print("You got it right! Onto the next word...")


    def question2(self):
      questions_tally = 3
      words_tally = 3
      qa2 = input("What is 6/(2(1+2))? ")
      if questions_tally <= 0 or words_tally <= 0:
        print("Game Over.")
        while qa2 != 1 or qa2.lower() != "one":
            questions_tally -= 1
            qa2 = input("What is 6/(2(1+2))? ")

        if qa2 == 1 or qa2.lower() == "one":
            wa2 = input("What was the second word? ")
            while wa2.lower() != self.words[1]:
                words_tally -= 1
                print("Sorry, that was incorrect, please try again!")
                print(f'You have {words_tally} questions left')
                wa2 = input("What was the second word? ")
                    
        if wa2.lower() == self.words[1]:
            print("You got it right! Onto the next word...")
      

    def question3(self):
      questions_tally = 3
      words_tally = 3
      qa3 = input("Who was the second president of the United States? ")
      if questions_tally <= 0 or words_tally <= 0:
        print("Game Over.")
        while qa3.lower() != "john adams":
            questions_tally -= 1
            qa3 = input("Who was the second president of the United States? ")

        if qa3 == 1 or qa3.lower() == "one":
            wa3 = input("What was the third word? ")
            while wa3.lower() != self.words[2]:
                words_tally -= 1
                print("Sorry, that was incorrect, please try again!")
                print(f'You have {words_tally} questions left')
                wa3 = input("What was the third word? ")
                    
        if wa3.lower() == self.words[2]:
            print("You got it right! Onto the next word...")


    def question4(self):
      questions_tally = 3
      words_tally = 3
      qa4 = input("What shape is generally used for stop signs? ")

      if questions_tally <= 0 or words_tally <= 0:
        print("Game Over.")
        while qa4.lower() != "john adams":
          questions_tally -= 1
          qa4 = input("What shape is generally used for stop signs? ")

        if qa4.lower() == "octagon":
            wa4 = input("What was the fourth word? ")
            while wa4.lower() != self.words[3]:
                words_tally -= 1
                print("Sorry, that was incorrect, please try again!")
                print(f'You have {words_tally} questions left')
                wa4 = input("What was the fourth word? ")
                    
        if wa4.lower() == self.words[3]:
            print("You got it right! Onto the next word...")


    def question5(self):
      questions_tally = 3
      words_tally = 3
      qa5 = input("How many continents are there on Earth? ")

      if questions_tally <= 0 or words_tally <= 0:
        print("Game Over.")
        while qa5 != 7 or qa5.lower() != "seven":
            questions_tally -= 1
            qa5 = input("How many continents are there on Earth? ")

        if qa5 == 7 or qa5.lower() == "seven":
            wa5 = input("What was the fifth word? ")
            while wa5.lower() != self.words[4]:
                words_tally -= 1
                print("Sorry, that was incorrect, please try again!")
                print(f'You have {words_tally} questions left')
                wa5 = input("What was the fifth word? ")
                    
        if wa5.lower() == self.words[2]:
            print("You got it right! Onto the next word...")

                
words = "apple", "orange", "banana", "tomato", "grape"
mg = MemoryGame(words, interval)

print(mg.display_words(0))
print(mg.question1())

print(mg.display_words(1))
print(mg.question2())

print(mg.display_words(2))
print(mg.question3())

print(mg.display_words(3))
print(mg.question4())

print(mg.display_words(4))
print(mg.question5())
