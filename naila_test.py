import random

class GuessTheNumber:
    """
    Class that contains all the logic related to the "Guess the number" game

    Attributes:
        tries (int): number of allowed tries
        hints (int): number of hints that the player can use
    """
    def __init__(self, tries = 10, hints_left = 3):
        self.tries = tries
        self.hints_left = hints_left

    def hints(self, target_number):
        """
        This method handles providing hints to the user

        Args:
            target_number (int): the target number of the game (i.e. the number that the
                user is trying to guess)

        Side effects:
            Prints a hint to the standard output
            Updates the number of hints left
        """
        
        if self.hints_left ==  3:
            upper = target_number + 20
            lower = target_number - 20 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
                
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
        
        elif self.hints_left == 2:
            upper = target_number + 10
            lower = target_number - 10 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
            
        
        elif self.hints_left == 1:
            upper = target_number + 5
            lower = target_number - 5 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print (f"Number is between {lower} and {upper}\n")
            self.hints_left -= 1
        
        else:
            upper = target_number + 5
            lower = target_number - 5 
            
            if upper > 50:
                upper = 50
            if lower < 1:
                lower = 1
            print(f"You already used your guesses. Reminder number is between {lower} and {upper}")
            
    def mechanics_of_game(self, lower_bound = 1, upper_bound = 50):
        """
        This method handles the logic of the game

        Args:
            lower_bound (int): the lower bound of the target integer. Defaults to 1
            upper_bound (int): the upper bound of the target integer. Defaults to 50

        Side effects:
            Prints the game state and input prompts to the standard output
            Prints the result of the game
        """
        target_number = random.randint(lower_bound, upper_bound)
        print("The number you are looking for is between {} and {}".format(lower_bound, upper_bound))
        correctly_guessed = False
        i = 0
        while i < self.tries:
            user_input = input("Make a guess (or type 'H' to get a hint): ")
            if user_input == 'H':
                self.hints(target_number)
            elif user_input.isnumeric():
                guess = int(user_input)
                if guess == target_number:
                    correctly_guessed = True
                    break
                else:
                    print("Incorrect guess!")
            else:
                print("Wrong input!")
                continue
            i += 1
            
        if correctly_guessed:
            print("Correct guess! You won!")
        else:
            print("You ran out of tries; better luck next time!")

if __name__ == '__main__':
    gtn = GuessTheNumber()
    gtn.mechanics_of_game()
