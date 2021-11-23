def main():
    while games_won = 0
    games_attempted = 0 
    games=['memory game', 'jeopardy', 'guess the number']
    
    while games_won < 2 and games_attempted <= 3:
        choice = input(f'Which game would you like to play? /n {games}').lower()
        
        if choice == "jeopardy": 
            jg = Jeopardy(0)
            print(jg.play_jeopardy_game())
            games_attempted += 1 
            games('jeopardy').remove()
            
        elif choice == "memory game": 
            mg = MemoryGame(.5)
            print(mg.mechanics())
            games_attempted += 1 
            games('memory game').remove()
        
        elif choice == "guess the number": 
            gg = GuessTheNumber()
            print(gg.mechanics_of_game())
            games_attempted += 1
            games('guess the number').remove()
        
        else: 
            raise ValueError ("Sorry, that is not a valid game, try again!")
