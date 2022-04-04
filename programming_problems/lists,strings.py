# Program 1 --> Find the largest number in a list

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