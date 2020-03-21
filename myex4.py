# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
num = int(input("Give a number."))
x = range(1,num + 1)
div_list = []
for i in x:
    if num % i == 0:
        div_list.append(i)
print(div_list)