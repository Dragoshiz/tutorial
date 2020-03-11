from sys import argv

script, filename = argv

print("the file we're about to read is: {}".format(filename))
file = open(filename)
print("This is the shit:")
print(file.read())