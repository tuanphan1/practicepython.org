
word = 'EVAPORATE'
wordList = []

def guess():
    wordSplit = list(word)
    guessLetter = input("Guess a letter ")
    for i in range(len(wordSplit)):
        if guessLetter == wordSplit[i]:
            wordList[i] = guessLetter + " "

def startGame():
    gameOver = False
    print("Welcome to Hangman!")
    for i in range(len(word)):
        wordList.append('- ')
    
    while not gameOver:
        guessString = ''.join(wordList)
        print(guessString)
        guess()
        if '- ' not in wordList:
            gameOver = True

startGame()