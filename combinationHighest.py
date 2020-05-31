def combinationHighest(inputList,partialSolution,target_value,start):
    if target_value==0:
        print(partialSolution)
        return
    if start ==len(inputList):
        return
    for i in range(start,len(inputList)):
        combination=inputList[i]
        if combination >target_value or (i>start and combination == inputList[i-1]):
            continue
        partialSolution.append(combination)
        combinationHighest(inputList,partialSolution,target_value-combination,i+1)
        partialSolution.pop()


def main():
    IN=[1,1,2,5,6,7,10]
    USED=[]
    IN=sorted(IN)
    combinationHighest(IN,[],8,0)

if __name__ == '__main__':
    main()
