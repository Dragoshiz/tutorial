def chees_and_crackers(chees_count, boxes_of_crackers):
    print("you have {} cheeses".format(chees_count))
    print("you have {} boxes of crackers".format(boxes_of_crackers))
    print("man that's enough for a party")
    print("get a blanket. \n")


print("we can joust give the function numbers directly: ")
chees_and_crackers(20, 30)


print("OR we can use variables from our script: ")
amount_of_chees = 10
amount_of_crackers = 50

chees_and_crackers(amount_of_chees, amount_of_crackers)


print("we can even do math inside too: ")
chees_and_crackers(10 + 20, 5 + 6)


print("and we can combine the two, variables and math: ")
chees_and_crackers(amount_of_chees + 100, amount_of_crackers + 1000)
