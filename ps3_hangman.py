# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = \
"/home/human/edX/6.00.1x/Python Problem Sets/PS3 Hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()




#===1===1===1===1===1===1===1===1===1===1===1===
#Debugging and Testing
#===1===1===1===1===1===1===1===1===1===1===1===



#===1===1===1===1===1===1===1===1===1===1===1===
#Initializations
#===1===1===1===1===1===1===1===1===1===1===1===
alpha=string.ascii_lowercase


#===1===1===1===1===1===1===1===1===1===1===1===
#Functions
#===1===1===1===1===1===1===1===1===1===1===1===
'''
def secretToDict(secretWord):
    # makes the secret word into a dictionary, since letter frequency
    # doesn't matter except binary yes or no
    assert type(secretWord) == str, "err1: %r not of type str; secretToDict\
     requires a str" % getGuessedWord
    secretDict = {}
    for letter in secretWord.lower():
        secretDict[letter] = 1
    return secretDict
'''
def br():
    print("-----------")


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    assert type(secretWord) == str, "err2: %r not of type str; isWordGuessed\
     requires a str" % getGuessedWord
    assert type(lettersGuessed) == list, "err3: %r \is not of type list;\
     isWordGuessed\ requires a list" % lettersGuessed
    if len(lettersGuessed) == 0:
        return False
    for letter in secretWord:
        if not letter in lettersGuessed:
            return False
    return True
        
        
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    assert type(secretWord) == str, "err4: %r not of type str; getGuessedWord\
     requires a str" % getGuessedWord
    assert type(lettersGuessed) == list, "err5: %r \is not of type list;\
     getGuessedWord\ requires a list" % lettersGuessed
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    assert type(lettersGuessed) == list, "err6: %r \is not of type list;\
     getAvailableLetters requires a list" % lettersGuessed
    available = ''
    for letter in alpha:
        if letter in lettersGuessed:
            pass
        else:
            available += letter
    return available
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    assert type(secretWord) == str, "err7: you've given hangman something that\
     isn't a string: %r" % secretWord
    willing = True
    #One-time game load display
    print('Welcome to the game Hangman!')
    while willing == True:
        lettersGuessed=[]
        responseUnderstood = False
        guesses = 8
        #Display for start of each new game
        print('I am thinking of a word that is'\
            +str(len(secretWord))+' letters long')
        #print('Type \'quit\' at any time to quit.')
        br()
        while isWordGuessed(secretWord,lettersGuessed) == False and guesses > 0 and willing == True:
            guessValid = False
            guess = ''
            #Display for each turn
            print('You have '+str(guesses)+' guesses left')
            print("Available letters: " + getAvailableLetters(lettersGuessed))
            while guessValid == False and isWordGuessed(secretWord,lettersGuessed) == False:
                guess = raw_input('Please guess a letter: ').lower()
                if guess == 'quit':
                    willing = False
                    responseUnderstood = True
                    print('Exiting Hangman. Have a good one!')
                    break
                elif guess != 'quit' and len(guess) > 1:
                    print('Your guess is too long, enter just a single letter')
                elif len(guess) == 0:
                    print('Your guess is too short, enter one letter')
                elif guess not in alpha:
                    print('Please enter 1 of 26 English letters')
                elif len(guess) == 1:
                    if guess in lettersGuessed:
                        print('Oops! You\'ve already guessed that letter: '),
                        print getGuessedWord(secretWord,lettersGuessed)
                    else:
                        guessValid = True
                        lettersGuessed+=guess
                        if guess in secretWord:
                            print('Good guess: '),
                            print getGuessedWord(secretWord,lettersGuessed)
                        else:
                            guesses -= 1
                            print('Oops! That letter is not in my word: '),
                            print getGuessedWord(secretWord,lettersGuessed)
                else:
                    print("eep, I don't understand %r" % guess)
            br()
            #End of turn block
        if isWordGuessed(secretWord,lettersGuessed) == False:
            if willing == True:
                print('Sorry, you ran out of guesses. The word was %r.' % secretWord)
            else:
                print('btw, the word was %r.' % secretWord)
        else:
            print('Congratulations! You won!')
            
        while responseUnderstood == False:
            response = raw_input("Play again? [y]es, [n]o: ").lower()
            if response == 'n' or response == 'no' or response == 'quit':
                willing = False
                responseUnderstood = True
                print('Exiting Hangman. Have a good one!')
            elif response == 'y' or response == 'yes':
                willing = True
                responseUnderstood = True
                #secretWord = chooseWord(wordlist).lower()
            else:
                print("eep, I don't understand %r" % response)
        #End of new game block


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
