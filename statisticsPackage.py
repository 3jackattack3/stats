def add(num1, num2):
    return num1+num2

def average(list):
    mean = 0
    for counter in range(len(list)):
        mean+=list[counter]
    return mean/len(list)

print(add(2,6))
print(average([4,4,6,10]))
