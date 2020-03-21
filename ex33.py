i = 0
numbers = []

def funct(i, arg):
    num  = 6
    for i in range(0,6,arg):
        print("At the top i is {}".format(i))
        numbers.append(i)
        i = i + arg
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))
        print("the numbers: ")
        for num in numbers:
            print(num)
funct(1,1)