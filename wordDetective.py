def wordDetective(inputString,wordDictionary,partialSolution):
    if len(inputString)==0:
        print(partialSolution)
        return
    for i in range(0,len(inputString)):
        word=inputString[:i+1]
        if word in wordDictionary:
            partialSolution.append(word)
            wordDetective(inputString[i+1:],wordDictionary,partialSolution)
            partialSolution.pop()

def main():
    Input="catsanddog"
    dictionaryAsList =["cat","cats","and","sand","dog"]
    wordDetective(Input,dictionaryAsList,[])

if __name__ == '__main__':
    main()
