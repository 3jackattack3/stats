def add(num1, num2):
    return num1+num2

def average(list):
    mean = 0
    for counter in range(len(list)):
        mean+=list[counter]
    return mean/len(list)

def median(list):
    list.sort()
    if(len(list)%2 = 1):
        return list[(len(list)+1)/2]
    else:
        return average(list[len(list)/2], list[len(list)/2+1])

print(add(2,6))
print(average([4,4,6,10]))
