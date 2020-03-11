from sys import argv   
# u import from system the argv
script, input_file = argv
# this function prints the file
def print_all(f):
    print(f.read())
# n am inteles aici?? ce face seek
def rewind(f):
    f.seek(0)
# this function prints one line 
def print_a_line(line_count, f):
    print(line_count, f.readline())
# this one is a variable  that opens the file you choose
current_file = open(input_file)

print("First let's print the whole file:\n")
# this calls the function print_all with the 
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# i didnt understand this fucking seek shit
rewind(current_file)

print("Let's print three lines:")
# didnt understand the last part.. something about that we print just the first 3 lines from the file ?
current_line = 1
print_a_line(current_line, current_file)

current_line += 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)