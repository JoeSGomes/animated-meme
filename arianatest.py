import sys
import time

class MemoryGame:
    """
    memory game where the player has to memorize 5 words
    Attributes:
        words(list): words to memorize
        t(int): time interval in seconds
    """
    def __init__(self,time, questions_tally = 3, words_tally = 3):
        self.words = ["apple", "orange", "banana", "tomato", "grape"]
        self.time = time
        self.questions_tally = questions_tally
        self.words_tally = words_tally
    def display_words(self, index):
        """
        displays  five words for the player to memorize, separated by t sec intervals
        Args:
            index(int): location of the word we are referring to in words
        """
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        time.sleep(self.time)
        print("Get Ready!")
        time.sleep(.2)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print(self.words[index])
        time.sleep(self.time)
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        
        x = ""
        return x
        
    def questions(self, index, question, question_answer):
        """
        allows user to answer five questions to throw them off reciting the words from memory
        Args:
            i(int): index for word in words
            q(string): question for the user to answer
            a(string): correct answer
        """

        word_answer = self.words[index]
        word_user_answer = ""

        print(f'Reminder: You have {self.questions_tally} tries left to guess the question answer\n')
        user_answer = input(question)

        while user_answer.lower() != question_answer:
            if user_answer.lower() != question_answer and self.questions_tally != 1:
                self.questions_tally -= 1
                print("Sorry, that was incorrect, please try again!\n")
                print(f'You have {self.questions_tally} tries left to guess the question answer\n')
                user_answer = input(question)
            else:
                self.questions_tally -= 1
                break

        if user_answer.lower() == question_answer:
            print("Correct, now onto guessing the word...")
            print(f'\nReminder: You have {self.words_tally} tries left to guess the word\n')
            word_user_answer = input("What was the word? ")
            while word_user_answer.lower() != word_answer and self.words_tally != 1:
                self.words_tally -= 1
                print("Sorry, that was incorrect, please try again!\n")
                print(f'You have {self.words_tally} tries left to guess the word\n')
                word_user_answer = input("What was the word? ")
        
            if word_user_answer.lower() == word_answer:
                print("\nYou got it right, onto the next challenge!")
                time.sleep(self.time) 
                    
        if word_user_answer != word_answer:
            self.words_tally -= 1     
                  
        if self.questions_tally < 1 or self.words_tally < 1:
            print("Sorry, that was incorrect, and you ran out of tries!\n")
            print("\nYou lost. Better luck next time!")
            
        
        x = ""  
        return x  


    def mechanics(self):
        dictionary_questions = {1 : "What is the first element in the periodic table? ",
                                2 : "What is the last letter of the alphabet? ",
                                3 : "Who was the second president of the United States? ",
                                4 : "What shape is generally used for stop signs? ",
                                5 : "Who won the 2021 World Series? "}
        questions_key = 1
        
        dictionary_answers = {1 :"hydrogen",
                            2 : "z",
                            3 : "john adams",
                            4 : "octagon",
                            5 : "braves"}
        answer_key = 1
        
        index = 0
        
        while self.questions_tally > 0 and self.words_tally > 0 and index <= 3:
            self.display_words(int(index))
            self.questions(int(index), dictionary_questions[questions_key], dictionary_answers[answer_key])
            questions_key += 1
            answer_key += 1
            index += 1
        

            
        x = ""
        return x

mg = MemoryGame(1)
print(mg.mechanics())