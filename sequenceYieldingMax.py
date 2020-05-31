import time
all_solutions=[]

def sequenceYieldingMax(inputList,partialSolution,target_value,start):
    if target_value==0:
        all_solutions.append(partialSolution.copy())
        return
    elif start>len(inputList):
        return
    for i in range(start,len(inputList)):
        choosenOne=inputList[i]
        if choosenOne>target_value:
            continue
        partialSolution.append(choosenOne)
        sequenceYieldingMax(inputList,partialSolution,target_value-choosenOne,start+1)
        partialSolution.pop()

def removingDuplicates(all_solutions):
    sortedList=[]
    for i in all_solutions:
        sortedList.append(sorted(i))
    return [i for n, i in enumerate(sortedList) if i not in sortedList[:n]]

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
    print("without the repetation following are the results")
    start_time = time.time()
    sequenceYieldingMax(IN,[],8,0)
    finalResults=removingDuplicates(all_solutions)
    for i in finalResults:
        print (i)
    print("--- %s seconds in my method---" % (time.time() - start_time))
    start_time = time.time()
    combinationHighest(IN,[],8,0)
    print("--- %s seconds in their method---" % (time.time() - start_time))
if __name__ == '__main__':
    main()
