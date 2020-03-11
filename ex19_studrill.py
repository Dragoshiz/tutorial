def workdays(worked, free):
    print("I have worked {} dayz".format(worked))
    print("I used {} freedays".format(free))
    days = int(worked) + int(free)
    print("The total of days are {}" .format(days))

def calc():
    work = int(input("how much did u work? "))
    free = int(input('how much free u have? '))
    total = work + free
    print("the total is {} days " .format(total))
    if free < 21:
        work = 240 - 21 - free
        print("You have {} work and {} free".format(work, free))
    elif work > 240:
        free = free + work - 240
        print("You have {} work and {} free".format(work, free))
calc()