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