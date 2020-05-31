import time

def permutationAnagram(inputString,partialSolution,flags):
    if len(partialSolution)==len(inputString):
        print(partialSolution)
        return
    for i in range(len(inputString)):
        if not flags[i]:
            partialSolution+=(inputString[i])
            flags[i]=True
            permutationAnagram(inputString,partialSolution,flags)
            flags[i]=False
            partialSolution=partialSolution[:-1]

def permutationAnagramSolution(inputString,partialSolution,flags,index):
    if index==len(inputString):
        string=''.join(str(e) for e in partialSolution)
        print(string)
        return
    for i in range(0,len(inputString)):
        if not flags[i]:
            flags[i]=True
            partialSolution.append(inputString[i])
            permutationAnagramSolution(inputString,partialSolution,flags,index+1)
            flags[i]=False
            partialSolution.pop()

def main():
    IN="god"
    USED=[]
    for i in range(len(IN)):
        USED.append(False)
    start_time = time.time()
    permutationAnagram(IN,"",USED)
    print("--- %s seconds in my method---" % (time.time() - start_time))
    print("\n")
    INList=list(IN)
    start_time = time.time()
    permutationAnagramSolution(INList,[],USED,0)
    print("--- %s seconds in their method---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
