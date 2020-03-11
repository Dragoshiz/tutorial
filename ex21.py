def add(a,b):
    print("ADDING {} + {}".format(a,b))
    return a + b

def substract(a, b):
    print("SUBSTRACTING {} + {}".format(a,b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING {} * {}".format(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING {} / {}".format(a,b))
    return a / b


print("Let's do some math with just functions! ")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))


print("Here is a puzzle.")


what = add(age, substract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "can you do it by hand?")
fuck = 35 + (74-(180*(50/2)))
print(fuck)