import random

class GuessTheNumber:
    """
    Class that contains all the logic related to the "Guess the number" game

    Attributes:
        tries (int): number of allowed tries
        hints (int): number of hints that the player can use
    """
    def __init__(self, tries = 10, hints = 3):
        self.tries = tries
        self.hints = hints

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
        for i in range(self.tries):
            guess = int(input("Make a guess: "))
            if guess == target_number:
                correctly_guessed = True
                break
            else:
                print("Incorrect guess!")
            
        if correctly_guessed:
            print("Correct guess! You won!")
        else:
            print("You ran out of tries; better luck next time!")
