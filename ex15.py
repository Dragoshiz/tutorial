# you import argument variables from system
from sys import argv

# you give variables to the argv
script, filename = argv

# you give the path to the file in a variable
txt = open(filename)

# this is a fucking print
print("Here's your file {}: ".format(filename))
# you read the file
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)
txt.close()
txt_again.close()
print(txt_again.read())
