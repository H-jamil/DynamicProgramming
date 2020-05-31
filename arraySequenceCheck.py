import time


def arraySequenceCheck(targetArray,index):
    if index==len(targetArray)-1:
        return True
    elif targetArray[index]+1==targetArray[index+1]:
        return True and arraySequenceCheck(targetArray,index+1)
    else:
        return False


def sumOfDigits(number,index):
    if index==0:
        return int(number[index])
    return int(number[index])+sumOfDigits(number,index-1)

def sumOfDigitsNumerical(number):
    if number==0:
        return 0
    return int(number%10)+sumOfDigitsNumerical(number/10)

def isPalindrome(text,first,last):
    if first==last: #for odd numbers of length
        return True
    elif last==first+1: # for even numbers of length
        if text[first]==text[last]:
            return True
        else:
            return False
    elif text[first]==text[last]:
        return True and isPalindrome(text,first+1,last-1)
    else:
        return False

def main():
    array1=[2,3,4,5,6,7,8]
    array2=[2,3,5,6,7,8]
    print(arraySequenceCheck(array1,0))
    print(arraySequenceCheck(array2,0))
    number="12345678910"
    numberNumerical=12345678910
    start_time = time.time()
    print(sumOfDigits(number,len(number)-1))
    print("--- %s seconds in string---" % (time.time() - start_time))
    start_time2 = time.time()
    print(sumOfDigitsNumerical(numberNumerical))
    print("--- %s seconds in number---" % (time.time() - start_time2))
    text="abbbabbba"
    text1="abbcabbba"
    text2="acca"
    text3="aca"
    text4="acb"
    text5="acda"

    print(text +" is "+ str(isPalindrome(text,0,len(text)-1)))
    print(text1 +" is "+str(isPalindrome(text1,0,len(text1)-1)))
    print(text5 +" is "+str(isPalindrome(text5,0,len(text5)-1)))
    print(text3 +" is "+str(isPalindrome(text3,0,len(text3)-1)))
    print(text4 +" is "+str(isPalindrome(text4,0,len(text4)-1)))
    print(text2 +" is "+str(isPalindrome(text2,0,len(text2)-1)))

if __name__ == '__main__':
    main()
