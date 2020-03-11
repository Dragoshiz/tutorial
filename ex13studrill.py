from sys import argv

numbers = argv[1:]
"""
Another way is: 
total = sum([int(num) for num in argv[1:]])
"""
total = 0
for num in numbers:
    total = total + int(num)
print("The total of the arguments: ", total)
d_input = int(input("write a fucking number to multiply it with: "))
result = d_input * total
print(result)

if result > 0:
    print("FASZOMBA BELE SIKERULT")



