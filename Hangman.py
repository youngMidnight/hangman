#!/usr/python
import random 
# Hangman_PICS is a Constant variable 

Hangman_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
 O  |
    |
    |
   ===''', '''
+---+
  O |
  | |
    |
   ===''', '''
+---+
  O |
 /| |
    |
   ===''', '''
+---+
 O  |
/|\ |
    |
   ===''', '''
+---+
 O  |
/|\ |
/   |
   ===''', '''      
+---+
 O  |
/|\ |
/ \ |
   ===''']


words =  'ant baboon badger bat bear beaver camel cat clam cobra cougarcoyote crow deer dog donkey duck eagle ferret fox frog goat goose hawklion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheepskunk sloth snake spider stork swan tiger toad trout turkey turtleweasel whale wolf wombat zebra'.split()

def getRandomWord(WordList):
    WordIndex=random.randint(0, len(WordList) - 1)
    return WordList[WordIndex]

def displayBoard(missedLetters,correctLetters,secrectWord):
   
    print(Hangman_PICS[len(missedLetters)])
    print()
   

    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
             print('You have alredy guessed that letter.')
        else:
            return guess


def PlayAgain():
 
     print(' Do you want to play again? ( Yes or No)')
     return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters =''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters,correctLetters,secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
             print(' yest the secret word is "'+ secretWord + '"! You have won!')
             gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(Hangman_PICS)-1:
               displayBoard(missedLetters, correctLetters,secretWord)
               print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str (len(correctLetters)) + ' + correct guesses, the word was'+ secretWord)
               gameIsDone = True
        else:
            missedLetters = missedLetters + guess

# Check if player has guessed too many times and lost.
        if len(missedLetters) == len(Hangman_PICS) - 1:
           displayBoard(missedLetters, correctLetters, secretWord)
           print('You have run out of guesses!\nAfter ' +
                   str(len(missedLetters)) + ' missed guesses and ' +
                   str(len(correctLetters)) + 'correct guesses,the word was ', secretWord +'"')
           gameIsDone = True

   # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if PlayAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break

       

