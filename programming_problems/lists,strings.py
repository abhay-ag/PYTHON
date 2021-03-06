# Program 1 --> Find the largest number in a list

from types import resolve_bases


def largestList(li):
    bigNum = li[0]
    for i in range (0,len(li)):
        if(li[i] > bigNum):
            bigNum = li[i]
    print("Biggest number: ", bigNum)

li = [1,2,3,34,4,4,4112,222,221,13]

largestList(li)

# Program 2 --> Reverse a list

def revLis(li):
    for i in range (0, len(li)):
        for j in range(i+1, len(li)):
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
        
    print(li)

revLis(li)

# Program 3 --> If an element exists in list

def inList(li, ele):
    flag = False
    for i in range(0, len(li)):
        if(ele == li[i]):
            flag = True
            break

    if flag:
        print("Element found")
    else: print("Not found")

inList(li, 3112)

# Program 4 --> Running total of a list

def runningSum(li):
    sum = 0
    for i in range(0, len(li)):
        sum += li[i]
        print(sum)

runningSum(li)

# Program 5 --> Elements at odd positions of an array

def oddPosition(li):
    for i in range(1, len(li), 2):
        print(li[i], end= ' ')
    print()

oddPosition(li)

# Program 6 --> Palindrome string

def palindrome(str):
    if (str == str[::-1]):
        print("String is Palindrome")
    else: print("Not palindrome")

palindrome('nam')

# Program 7 --> sum of array WHILE, FOR, RECURSION

def sumFor (li):
    sum = 0
    for i in range(0, len(li)):
        sum += li[i]
    
    print(sum, "FOR LOOP")

def sumWhile(li):
    sum = 0
    i = len(li) -1
    while i >=0:
        sum += li[i]
        i -= 1
    print(sum,"WHILE LOOP")

def sumRec(li , start, end):
    if (start > end):
        return 0
    else:
        return (li[start] + sumRec(li, start + 1, end))
    

sumFor(li)
sumWhile(li)
sumRecusive = sumRec(li, 0, len(li)-1)
print(sumRecusive, "RECURSION")

# Program 8 --> concat two lists

def concats(li,li1):
    print(li + li1)

concats(li, [1,2,2,3,3,5])

# Program 9 --> concat alternate elements

def concatAlt(li, li1):
    resLi = []
    for i in range(0, len(li)):
        resLi.append(li[i])
        resLi.append(li1[i])

    print(resLi)

concatAlt(['a','b','c'], [1,2,3])

# Program 10 --> Merge two sorted lists into a new sorted list

def mergeSort(arr1, arr2):
    resArr = arr1 + arr2
    bigNum = resArr[0]

    for i in range(0, len(resArr)):
        for j in range(i+1, len(resArr)):
            if (resArr[i] > resArr[j]):
                resArr[i], resArr[j] = resArr[j], resArr[i]
    
    print(resArr)

mergeSort([1,4,6], [2,3,5])

# Program 11 --> Rotate a list

def rotateLi(li,k):
    rotArray = []
    for i in range(k, len(li)):
        rotArray.append(li[i])
    for j in range(0, k):
        rotArray.append(li[j])
    
    print(rotArray)

rotateLi([1,2,3,4,5,6],3)

# Program 12 --> Fibonnaci series

def fib():
    first = 1
    second = 1
    resli =[first,second]
    for i in range(2, 100):
        third = first + second
        resli.append(third)
        first = second
        second = third
    print(resli)

# fib()

# Program 13 --> Spilt a number into individual digits

def splitNum():
    splitLi = int(input())
    splitLi = str(splitLi)
    resli = []

    for i in range (0, len(splitLi)):
        resli.append(int(splitLi[i]))

    print(resli)

splitNum()

# Program 14 --> Print a list in a frame

def frameList(li):
    index = 0 
    bigLetter = len(li[0])
    for i in range(0, len(li)):
        if (len(li[i]) > bigLetter):
            bigLetter = len(li[i])
            index = i
    for i in range(0, len(li)):
        if(i == 0):
            print("*"*(len(li[index]) +4))
        print("*", li[i], " "*(len(li[index]) - len(li[i])), "\b*")
        if(i == len(li)-1):
            print("*"*(len(li[index]) +4))

frameList(["Hello", "World", "in", "a", "frame"])