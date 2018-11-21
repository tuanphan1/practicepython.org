import random

word = ''
wordList = []

def getWord():
    with open('sowpods.txt') as wordFile:
        lines = wordFile.readlines()
        lineNumber = random.randint(0,267751)
        word = lines[lineNumber]
        wordFile.close
        return word
        
def guess(word, guessLeft):
    foundChar = False
    wordSplit = list(word)
    guessLetter = input("Guess a letter ")
    for i in range(len(wordSplit)):
        if guessLetter == wordSplit[i]:
            wordList[i] = guessLetter + " "
            foundChar = True
    if foundChar == False:
        guessLeft = guessLeft - 1
        print("you have " + str(guessLeft) + " guesses left")
        if guessLeft == 0:
            print("You lose game over") 
    return guessLeft

def startGame():
    gameOver = False
    guessLeft = 5
    print("Welcome to Hangman!")
    word = getWord()
    word = word.strip()
    print(word)
    for i in range(len(word)):
        wordList.append('- ')
    
    while not gameOver:
        guessString = ''.join(wordList)
        print(guessString)
        guessLeft = guess(word, guessLeft)
        if '- ' not in wordList:
            gameOver = True

if __name__ == "__main__":
    startGame()