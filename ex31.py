print("you enter a dark room with two doors. Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a chees cake. What do you do?")
    print("1. take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. Good job shithead")
    elif bear == "2":
        print("The bear eats your legs off. Good job fucker")
    else:
        print("Well, doing {} is probably better. Bear runs away.".format(bear))

elif door == "2":
    print("you stare into the endless abyss at cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello. Fasza.")
    else:
        print("The insanity rots your eyes into a pool of muck. great.")

else:
    print("you stamble around and fall on a knife and die. noice")
    