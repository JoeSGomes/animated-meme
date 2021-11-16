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
        
    def questions(self, i, q, a):
      qa = input(q)
      questions_tally = 0
      words_tally = 0

      while qa.lower() != a or qa != a:
        questions_tally =  questions_tally - 1
        qa = input(q)

      if qa.lower() == a:
          wa = input("What was the word? ")
          while wa.lower() != self.words[i]:
              words_tally = words_tally - 1
              print("Sorry, that was incorrect, please try again!")
              print(f'You have {words_tally} questions left')
              wa = input("What was the word? ")
              
      if wa.lower() == self.words[i]:
          print("You got it right! Onto the next word...")


                
words = ["apple", "orange", "banana", "tomato", "grape"]
q1 = "What is  the first element in the periodic table? "
a1 = "hydrogen"
q2 = "What is the last letter of the alphabet? "
a2 = "z"
q3 = "Who was the second president of the United States? "
a3 = "john adams"
q4 = "What shape is generally used for stop signs? "
a4 = "octagon"
q5 = "Who won the 2021 World Series? "
a5 = "braves"

mg = MemoryGame(words, interval)

print(mg.display_words(0))
question_set1 = mg.questions(0, q1, a1)
print(question_set1)

print(mg.display_words(1))
question_set2 = mg.questions(1, q2, a2)
print(question_set2)

print(mg.display_words(2))
question_set3 = mg.questions(2, q3, a3)
print(question_set3)

print(mg.display_words(3))
question_set4 = mg.questions(3, q4, a4)
print(question_set4)

print(mg.display_words(4))
question_set5 = mg.questions(4, q5, a5)
print(question_set5)
