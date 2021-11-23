
from random import randint


#def __init__(self):
 #   self.lower = 30
  #  self.higher = 100
        
#def random_number(self):
  #  return randint(self.lower, self.higher)
    
def hints(counter, number): 
    ''' this method gives 3 separate hints for player if requested
        
        Args: 
            counter(int): counter starts at 0, each time player prompts 'hint' 1 is added to counter to
                          total 3 at the end.
            number(int): the random number generated, will be added or subtracted or added by hint '''
	
    if counter ==  1: 
        print (f"Number is between {number - 20} and {number + 20}")
        
    elif counter == 2:
        print (f"Number is between {number - 10} and {number + 10}")
        
    elif counter == 3:
        print (f"Number is between {number - 5} and {number + 5}")
        
    else:
        print(f"You already used your guesses. Reminder number is between {number - 5} and 	{number + 5}")

def main():
    number = randint(30, 100)
    counter = 1
    hints(counter, number)
    counter = 2
    hints(counter, number)
    counter = 3
    hints(counter, number)
    counter = 4 
    hints(counter, number)

main()