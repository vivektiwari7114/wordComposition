# Basic Program Needs
import os
import copy

def getTheListOfFiles(rootDir):
    nameOfFiles =[]
    for root, dirs, files in os.walk(rootDir):
            for name in files:
                if name.endswith((".txt")):
                    nameOfFiles.append(name)
    return nameOfFiles

#Open individual File and Read the Words and store in dictionary
def openIndividualFile(fileName, tempDict):
    fileContent = open(fileName, "r").read()
    listOfWords = fileContent.split()
    for word in listOfWords:
        sWord = word.lower()
        tempDict[sWord] = len(sWord)
    return tempDict

#Algorithm for checking whether the string  is the contituents of the given dictionary
def checkWordComposition(word, wordsDict):
        check =[]
        for i in range (0,len(word) + 1):
                check.append(0)
        check[0] = 1

        for i in range(len(check)):
            if check[i] == 0:
                continue
            for j in range(i+1, len(check)):
                subString = word[i:j]
                if subString in wordsDict:
                    check[j] = 1
        return check[len(check) - 1]



# Main Program Executes Here
nameOfFiles = getTheListOfFiles(".")
wordsDict = {}
finalList =[]
for files in nameOfFiles:
    wordsDict = openIndividualFile(files,wordsDict )
#Sort the Dictionary in Decreasing order of the len of Words
listOfProcessedWords =  sorted(wordsDict, key = wordsDict.get, reverse=True)

for words in listOfProcessedWords:
    tempDict = copy.deepcopy(wordsDict)
    del tempDict[words]
    if checkWordComposition(words, tempDict)  == 1:
            finalList.append(words)
            if len(finalList) == 2:
                break

#Print the Final Output
print (finalList)


