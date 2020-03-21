people = 30
cars = 40
buses = 15


if cars > people:
    print("we should take the cars.")
elif cars < people:
    print("we should not take the cars.")
else:
    print("we can't decide.")

if buses > cars:
    print("too many busses.")
elif buses < cars:
    print("Maybe we could take the busses.")
else:
    print("We stll can't decide.")

if people > buses:
    print("alright, let's just take the buses.")
else:
    print("fine, let's stay home then.")
