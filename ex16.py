from sys import argv

script, filename = argv

print("We're going to erase {}.".format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye fucker!!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

list = [line1, line2, line3]

for l in list:
    target.write(l + "\n")

print("And finally, we close it.")
target.close()