# Program 1

def falling_distance(time):             # Defining The function falling_distance
    g = 9.8
    return (g * (time**2))/2            # The funtcion returns the falling distance in meters

for i in range (1, 11):
    distance = falling_distance(i)      # The return value is stored inside of distance variable
    print(f"{distance:.2f} meteres")    # The Value is printed using a f-String to reduce the number of decimal points

# Program 2

def calc_average(m1, m2, m3, m4, m5):       #Defining the average calculator function
    avg = (m1 + m2 + m3 + m4 + m5) // 5
    return avg

def determine_grade(avgMarks):              #Defining the grade determining function
    if (avgMarks >= 90 and avgMarks <= 100):
        return "A"
    elif (avgMarks >=80 and avgMarks <= 89):
        return "B"
    elif (avgMarks >= 70 and avgMarks <= 79):
        return "C"
    elif (avgMarks >= 60 and avgMarks <=69):
        return "D"
    else:
        return "E"
li = []                                     
for i in range(0, 5):
    marks = int(input("Enter the marks in individual subject: "))   #Taking input in the form of a list
    li.append(marks)

m1, m2, m3, m4, m5 = li                     #Destructuring the list to five variables

avgMarks = calc_average(m1, m2, m3, m4, m5)

grade = determine_grade(avgMarks)

print(grade, " grade achieved")             #Printing the result

# Program 3

def is_prime(number):                       #Defining the function to check if a number is prime
    flag = False
    for i in range (2, number):
        if (number % i == 0):
            flag = True
            break                           #If a number is not prime then the loop breaks here and flag is set to True

    if flag:                                #If flag is true then False is returned else True is returned
        return False
    else: 
        return True

num_check = int(input("Enter the number to be checked if it is prime: "))

res = is_prime(num_check)

if (res):
    print(num_check, "is Prime.")
else:
    print(num_check, "is not Prime")

# Program 4

def check_list(li):                         #Defining the function
    bigNum = -9999999999                        #Assigning the largest number to smallest value
    smallNum = 9999999999                       #Assigning the smallest to largest value
    liSum = 0
    for i in li:
        if ( i > bigNum):
            bigNum = i              #Finding the biggest number
    
    for j in li:
        if ( j < smallNum):
            smallNum = j            #Finding the smallest number
    
    for k in li:
        liSum += k                  #Finding the sum of the list
    
    liAvg = liSum / len(li)         #Finding the average of the list

    return bigNum, smallNum, liSum, liAvg

list_check = []
for i in range( 0 , 20 ):
    var = int(input("Enter the number: "))
    list_check.append(var)

largestNum, smallestNum, sumList, avgList = check_list(list_check)

print("Largest Number in list: ", largestNum)
print("Smallest Number in list: ", smallestNum)
print("Sum of Numbers in list: ", sumList)
print("Average of Numbers in list: ", avgList)

# Program 5

def print_all_primes(num):                  # Defining the Function
    flag = False

    for i in range(2, num):                 #Check if a Number is prime
        if (num%i == 0):
            flag = True
            break

    if flag:                                #If it is prime then return Prime else return Composite
        return "Composite"
    else: 
        return "Prime"

element = 0
while not(element>1):               #Checking if the number is greater than one
    element = int(input("Enter a number greater than 1: "))

li_emp = []             #Initializing an empty list

for i in range(2, element + 1):
    li_emp.append(i)    #Populating the list with elements

for j in li_emp:        #Passing Individual elements of the list to the function
    res = print_all_primes(j)

    if res == "Prime":
        print( j, "\b: Prime")
    else:
        print( j, "\b: Composite")