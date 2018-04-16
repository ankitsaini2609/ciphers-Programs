UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERCASE+UPPERCASE.lower()+' \n\t'

def loadDictionary():
    dicobj = open('dictionary.txt','r')
    englishWords = {}
    for word in dicobj.read().split('\n'):
        englishWords[word] = None
    dicobj.close()
    return englishWords

English_Words = loadDictionary()

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in English_Words:
            matches += 1
    return float(matches)/len(possibleWords)

def isEnglish(message,wordPercentage = 20, letterPercentage=85):
    wordsMatch = getEnglishCount(message)*100 >= wordPercentage
    lettersMatch = (float(len(removeNonLetters(message)))/len(message)) * 100 >= letterPercentage
    return (wordsMatch and lettersMatch)
