def add(num1, num2):
    return num1+num2

def average(list):
    mean = 0
    for counter in range(len(list)):
        mean+=list[counter]
    return mean/len(list)

def median(list):
    list.sort()
    if(len(list)%2 == 1):
        return list[(int) ((len(list))/2)]
    else:
        return average([list[(int) (len(list)/2)], list[(int) (len(list)/2-1)]])

def mode(list):
    longestStreak = 0
    currentStreak = 0

    for counter in range(len(list)):
        if(list[counter] != list[counter+1]):

        if(longestStreak < currentStreak):
            longestStreak = currentStreak

def range:

def std:



print(add(2,6))
print(average([4,4,6,14]))
print(median([1,3,4,5,6]))
