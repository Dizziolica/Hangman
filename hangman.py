def hangman():
    import random
    words = ["Espanha", "Portugal", "França", "Alemanha", "Italia", "Holanda", "Irlanda"]
    word = random.choice(words)
    guess = []
    listwords = []
    listletters = []
    alphabet = "abcdefghijklmnopqrstuvxyz"
    trys = 6
    
    for i in word.lower():
        listwords.append(i)
        
    for j in alphabet:
        listletters.append(j)
        
    for o in range(len(word)):
        guess.append("")
        
    while trys > 0 and guess != listwords :
    
        print("Europe Country")
        
        guessuser = input("Guess the letter in the Country, digit one letter:   " )
            
        if guessuser in listwords:
            indices = []
            numbers = 0
     
            indexes = [i for i, x in enumerate(listwords) if x == guessuser]
                
            for i in indexes:
                guess[i] = guessuser
                    
                print(guess)
                       
                print(f"The letter is in the word {guess} ")
        else:
            trys -= 1
            print("Try again")
    
    if guess == listwords:
        print("You are right")
        guessfinal = ''.join(map(str,guess))
        print(guessfinal.capitalize())
    
    if trys == 0:
        print(f"You not answer right, the country is {word}")
        
hangman()
