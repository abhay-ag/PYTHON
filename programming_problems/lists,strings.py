# Program 1 --> Find the largest number in a list

def largestList(li):
    bigNum = li[0]
    for i in range (0,len(li)):
        if(li[i] > bigNum):
            bigNum = li[i]
    print("Biggest number: ", bigNum)

li = [1,2,3,34,4,4,4112,222,221,13]

largestList(li)