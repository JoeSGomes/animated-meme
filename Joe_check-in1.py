def available_questions(subject):
    """[summary]

    Args:
        subject ([type]): [description]

    Returns:
        [type]: [description]
    """
    dictionary = {'Pop Culture': {500: ('How many kids does Angelina Jolie have?', '6'),  
                                  300: ('How many fast and furious movies are there?', '9'), 
                                  200: ('Who is Jay-Z’s wife?', 'Beyonce'), 
                                  100: ('What is Justin Bieber’s top song?', 'baby')}, 
                  
              'Math': {500: ('What is the derivative of 60x^2', '120'), 
                       400: ('What is (40^2) x 8', '12800'), 
                       300: ('What is (25000/5) x 2', '10000'), 
                       100: ('What is 10^2?', '100')}, 
              
              'History': {500: ('Who invented the first electric automobile? (no spaces)', 'robert anderson'), 
                          400: ('What year did the american revolution start', '1775'),  
                          200: ('What year did Christopher Columbus discover America?', '1492'), 
                          100: ('Who gave the statue of liberty to the united states', 'France')}}
    place = dictionary.get(subject)
    keys = place.keys()
    l = []
    for i in keys:
        l.append(i)
    return f'{subject} Questions Available: {l}'

print()
print (available_questions("Math"))
print()
print (available_questions("History")) 
print()
print (available_questions("Pop Culture"))
print()