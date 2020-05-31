def combinationWithBacktracking(inputList,partialSolution,size,start):
    if len(partialSolution)==size:
        print(partialSolution)
        return
    if start ==len(inputList):
        return
    partialSolution.append(inputList[start])
    combinationWithBacktracking(inputList,partialSolution,size,start+1)
    partialSolution.pop()
    combinationWithBacktracking(inputList,partialSolution,size,start+1)


def main():
    IN=[3,2,5,8]
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    combinationWithBacktracking(IN,[],3,0)

if __name__ == '__main__':
    main()
