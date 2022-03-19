# Program 1

def falling_distance(time):             # Defining The function falling_distance
    g = 9.8
    return (g * (time**2))/2            # The funtcion returns the falling distance in meters

for i in range (1, 11):
    distance = falling_distance(i)      # The return value is stored inside of distance variable
    print(f"{distance:.2f} meteres")    # The Value is printed using a f-String to reduce the number of decimal points