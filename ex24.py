print('Lets practice everything.')
print("you\'d need to know \'bout escapes with\\ that do \n newlines and \t tabs")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------")
print(poem)
print("-----------")


five = 10 - 2 + 3 - 6
print("This should be five: {}".format(five))
# function returns the results of jelly_beans, jars, crates 
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# These takes the return values
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))
print("We'd have {} beans, {} jars, and {} crates.".format(beans, jars, crates))

start_point = start_point / 10

print("We can alsodo that this way:")
print("We'd have {} beans, {} jars, and {} crates.".format(*secret_formula(start_point)))