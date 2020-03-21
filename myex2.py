# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#  Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num,
#  tell that to the user. If not, print a different appropriate message.

num = int(input("Give me a number. "))
rest = num % 2
four = num % 4
if rest > 0:
    print("You picked an odd number")
else:
    print("You picked an even number")
if four == 0:
    print("This is an multiple of four")
    
