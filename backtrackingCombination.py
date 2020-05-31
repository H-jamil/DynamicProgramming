def combinationWithBacktracking(inputList,partialSolution,flags,size):
    if len(partialSolution)==size:
        print(partialSolution)
        return
    for i in range(len(inputList)):
        if not flags[i]:
            partialSolution.append(inputList[i])
            flags[i]=True
            combinationWithBacktracking(inputList,partialSolution,flags,size)
            flags[i]=False
            partialSolution.pop()

def main():
    IN=[3,2,5,8]
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    combinationWithBacktracking(IN,[],USED,3)

if __name__ == '__main__':
    main()
