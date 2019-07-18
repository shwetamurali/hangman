from random_word import RandomWords
#test
print("Welcome to Hangman!")
print("Enter full word at any point if you know it.")
totalWins=0
stillPlaying=True
#word = input("What word do you want to guess? ").lower()
r=RandomWords()


def checkGuess(guess):
    global remainingAttempts
    global stillPlaying

    if guess in allGuesses:
        newGuess = input("You have already guessed " + guess +". Please guess another letter: " ).upper()
        checkGuess(newGuess)
    elif guess in word:
        print("Good job! " + str(guess) + " is in the word!")
        #print(''.join(correctGuesses))
        #correctGuesses[word.find(guess)]=guess #fix find method
        fillOccurrences(word,guess)
        allGuesses.append(guess)

    else:
        remainingAttempts-=1
        if guess not in allGuesses:
            allGuesses.append(guess)
        print("Sorry, " + str(guess) + " is not in the word.")
            #print(''.join(correctGuesses))
    #print("You have "+str(remainingAttempts)+" lives left.")

def checkWin():
    global hasWon
    if  " _ " not in correctGuesses:
        hasWon = True

def fillOccurrences(word, guess):
    global correctGuesses
    for i in range(0,len(word)):
        if word[i] == guess:
            correctGuesses[i]=" "+ guess + " "
while(stillPlaying):
    remainingAttempts = 6
    word = r.get_random_word(hasDictionaryDef="true",minLength=5).upper()
    #print(word)
    correctGuesses=[]
    allGuesses=[]
    for letter in word:
        correctGuesses.append(" _ ")
        #correctGuesses[word[start:].find(guess)]=guess
    hasWon = False    
    while(remainingAttempts>0 and not hasWon):
        print(''.join(correctGuesses))
        userGuess = input("Guess a letter: ").upper()
        if len(userGuess)>1:
            if(userGuess=="STOP"):
                stillPlaying=False
                break
            elif(userGuess.upper()==word):
                hasWon=True
                break
            else:
                remainingAttempts-=1
                print("Sorry, " + str(userGuess) + " is not the word.")
        else:    
            checkGuess(userGuess)
        if(remainingAttempts==1):
            print("You have " + str(remainingAttempts)+" life left.\n")
        else:
            print("You have " + str(remainingAttempts)+" lives left.\n")
        print("You have already guessed: " + str(allGuesses))
        checkWin()
    if(remainingAttempts==0):
        print("Sorry, you lose! The correct word is "+word)
    elif(hasWon):
        print(''.join(correctGuesses))
        totalWins+=1
        print("\nCongratulations! You win!")
    if(stillPlaying):
        keep=input("Do you want to keep playing? Y or N: ")
        if(keep.upper()=="N"):
            stillPlaying=False
            if(totalWins==1):
                print("You won the game "+str(totalWins)+" time.")
            else:
                print("You won the game "+str(totalWins)+" times.")
            break
        elif(keep.upper() !="Y"):
            print("Congratulations! You found the Easter egg. Keep the chain going!")
            stillPlaying=False
            break
