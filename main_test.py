def main():
    while games_won = 0
    games_attempted = 0 
    
    while games_won < 2 and games_attempted <= 3:
        choice = input('Which game would you like to play? /n Jeopardy , Memory Game , Guess the number?')
        
        if choice == "Jeopardy": 
            jg = Jeopardy(0)
            print(jg.play_jeopardy_game())
            games_attempted += 1 
            
        elif choice == "Memory Game": 
            mg = MemoryGame(.5)
            print(mg.mechanics())
            games_attempted += 1 
        
        elif choice == "Guess the Number": 
            gg = GuessTheNumber()
            print(gg.mechanics_of_game())
            games_attempted += 1 
        
        else: 
            raise ValueError ("Sorry, that is not a valid game, try again!")
