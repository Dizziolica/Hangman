def hangman():
    import random
    words = ["Espanha", "Portugal", "França", "Alemanha", "Italia", "Holanda", "Irlanda"]
    word = random.choice(words)
    guess = []
    listwords = []
    listletters = []
    points = 100
    alphabet = "abcdefghijklmnopqrstuvxyz"
    trys = 6
    
    for i in word.lower():
        listwords.append(i)
        
    for j in alphabet:
        listletters.append(j)
        
    for o in range(len(word)):
        guess.append("")
    
   
    while trys > 0 and guess != listwords:
    
        print("Europe Country")
        
        guessuser = input("Guess the letter in the Country, digit one letter:   " )
        print(word.lower())
        
        if str(guessuser.lower()) == str(word.lower()):
            print(f"You are right!, your {points} points")
        
        if len(guessuser) > 1 and str(guessuser.lower() )!= str(word.lower()):
            print("try again")
            trys -= 1
            
            
        if guessuser in listwords and len(guessuser) == 1:
            
            indexes = [i for i, x in enumerate(listwords) if x == guessuser]
                
            for i in indexes:
                guess[i] = guessuser
                    
                print(guess)
                       
                print(f"The letter is in the word {guess} ")
        if len(guessuser) == 1 and guessuser not in listwords:
            trys -= 1
            points -= 10
            print("Try again")
    
    if guess == listwords :
        print(f"You are right, your {points} points")
        guessfinal = ''.join(map(str,guess))
        print(guessfinal.capitalize())
    
    if trys == 0:
        print(f"You not answer right, the country is {word}")
    
   
        
hangman()
