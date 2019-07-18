print("Welcome to Hangman!")
remainingAttempts = 6
word = input("What word do you want to guess? ").lower()
correctGuesses=[]
for letter in word:
    correctGuesses.append(" _ ")
def checkGuess(guess):
    global remainingAttempts
    if guess in word:
        print("Good job! " + str(guess) + " is in the word!")
        print(''.join(correctGuesses))
        #correctGuesses[word.find(guess)]=guess #fix find method
        fillOccurrences(word,guess)
        
    else:
        remainingAttempts-=1
        print("Sorry, " + str(guess) + " is not in the word.")
        print(''.join(correctGuesses))
    print("You have "+str(remainingAttempts)+" tries left.")

def checkWin():
    global hasWon
    if  " _ " not in correctGuesses:
        hasWon = True

def fillOccurrences(word, guess):
    global correctGuesses
    for i in range(0,len(word)):
        if word[i] == guess:
            correctGuesses[i]=" "+ guess + " "
    #correctGuesses[word[start:].find(guess)]=guess
    
hasWon = False    
while(remainingAttempts>0 and not hasWon):
    print(''.join(correctGuesses))
    userGuess = input("Guess a letter ").lower()
    checkGuess(userGuess)
    checkWin()
if(remainingAttempts==0):
    print("Sorry, you lose! The correct word is "+word+".")
else:
    print(''.join(correctGuesses))
    print("Congratulations! You win!")
