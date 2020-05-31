def combinationWithBacktracking(inputList,partialSolution,size,start):
    if len(partialSolution)==size:
        print(partialSolution)
        return
    if start ==len(inputList):
        return
    for i in range(start,len(inputList)):
        partialSolution.append(inputList[i])
        combinationWithBacktracking(inputList,partialSolution,size,i+1)
        partialSolution.pop()


def main():
    IN=[3,2,5,8]
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    combinationWithBacktracking(IN,[],3,0)

if __name__ == '__main__':
    main()
