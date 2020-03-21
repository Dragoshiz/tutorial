from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to tipe a number.")
    
    if how_much < 50:
        print("Nice, you're not greedy, you get shit.")
        exit(0)
    else:
        dead("you greedy fucker!")
    

def bear_room():
    print("there is a bear here.")
    print("the bear have a bunch of honey")
    print("the fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("the bear looks at you then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print("the bear has moved from the door. You can go through now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews you")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("wtf is this")


def cthulu_room():
    print("here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was shit.")
    else:
        cthulu_room()
    

def dead(why):
    print(why,"good job, you dead")
    exit(0)

def start():
    print("you are in a dark room")
    print("There is a door to your right and left")
    print("Wich one do you take?")
    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("you stumble around the room until you starve.")


start()