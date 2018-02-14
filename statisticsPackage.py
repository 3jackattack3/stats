import math

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
    streakValue = 0
    #secondModeValue = 0

    for counter in range(len(list)-1):
        if(list[counter] != list[counter+1]):
            currentStreak = 0
        #if(currentStreak == longestStreak):
            #secondModeValue = list[counter]
        if(longestStreak < currentStreak):
            longestStreak = currentStreak
            streakValue = list[counter]
        currentStreak+=1

    #if(streakValue == secondModeValue):
    return streakValue

    #return [streakValue, secondModeValue]

def myRange(list):
    smallest = list[0]
    largest = list[0]

    for counter in range(len(list)):
        if(list[counter] < smallest):
            smallest = list[counter]
        if(list[counter] > largest):
            largest = list[counter]

    return largest-smallest


def std(list):
    Average = 0
    Average = average(list)
    std = 0

    for counter in range(len(list)):
        std += (list[counter] - Average)**2

    std /= len(list)

    return math.sqrt(std)

print(add(2,6))
print(average([4,4,6,14]))
print(median([1,3,4,5,6]))
print(mode([1,2,3,3]))
print(myRange([-1,2,3,5]))
print(std([1,2,3,4,5]))
#comment
#another comment
