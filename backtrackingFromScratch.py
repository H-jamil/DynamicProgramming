allSolutions=[]
def permutationWithBacktracking(inputList,partialSolution,flags):
    if len(partialSolution)==len(inputList):
        print(partialSolution)
        return
    for i in range(len(inputList)):
        if not flags[i] and not(inputList[i]==inputList[i-1] and not flags[i-1]):
            partialSolution.append(inputList[i])
            flags[i]=True
            permutationWithBacktracking(inputList,partialSolution,flags)
            flags[i]=False
            partialSolution.pop()

def main():
    IN=[1,4,1]
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    permutationWithBacktracking(IN,[],USED)

if __name__ == '__main__':
    main()
