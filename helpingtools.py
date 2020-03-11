"""
    TODO A FASZIKNAK:
        - create cheet-sheet
            - variables
            - data types
            - flow-control
            - looping
            - functions
            - imports
        - Show imports and basic module system
        - Show debugging
        - install sublack
​
"""
​
### VARIABLES
# <variable_name> = <data>
boolean_var = True
string_var = "String some String"
integer_var = 1000
float_var = 10.0
​
## dictionary
dictionary_dict = {
    "<_key>": "<value>",
    "another_key": "Another value for dictionary",
    "sadasdasd": "asdasdsadsasadasdasdasdas",
}
print(dictionary_dict["another_key"])  # => "Another value for dictionary"
dictionary_dict.get("another_key")  # => "Another value for dictionary"
print(dictionary_dict["not_existing_key"])  # => KeyError
dictionary_dict.get("not_existing_key")  # => None
dictionary_dict.get("not_existing_key", "default_value")  # => default_value
​
# get example
result = {}
for word in ["asd", "asd1", "asd"]:
    count = result.get(word, 0) + 1
    result[word] = count
​
​
## List
lista = ["123", "456", 789]
print(len(lista))  # => 3
print(lista[1])  # => 456
lista.append("101112")  # appends element to the list (at the back)
print(lista)  # => ["123", "456", 789, "101112"]
​
## complex
bod_peter = {
    "name": "bod_peter",
    "description": "Fasza",
    "teachers": [{"name": "Joska", "age": 40, "salary": 5000}, {"name": "Len Csaba", "age": 20, "salary": 5000}],
    "classes": {"IX": {"A": {"student_count": 25}, "B": {"student_count": 15}}},
}       
bod_peter["classes"]["IX"]["B"]["student_count"]  # => 15
bod_peter["teachers"][1]["name"]  # Len Csaba
​
​
### FUNCTION
def example_1():
    print("Hello")
​
​
# No return
example_1()  # => 'Hello'
result = example_1()  # => 'Hello'
print(result)  # => None
​
​
def example_2():
    print("Hello 2")
    return "Hello again"
    print("U cannot see this ever never ever")
​
​
# With return
example_2()  # => 'Hello 2'
result2 = example_2()
print(result2)  # => 'Hello again'
​
​
# Arguments
def example_3(arg_example):
    new_variable = "You called example_3 with {} arg".format(arg_example)
    print(new_variable)
​
​
example_3("this is my testing arg")  # => "You called example_3 with this is my testing arg arg"
res = example_3("something else")  # => "You called example_3 with something else arg"
print(res)  # => None
​
​
# multi argumentum
def summing_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3
​
​
summing_func(10, 20, 30)  # => Nothing because there is no print
print(summing_func(10, 20, 30))  # => 60
​
result_of_calling_the_function = summing_func(1, 2, 3)
print(result_of_calling_the_function)
​
​
# Control-flow
age = 10
​
if age < 20:
    print("kicsike")
else:
    print("whatever")
​
​
def positify(number):
    if number < 0:
        return -number
    return number
​
​
print(positify(-10))  # => 10
print(positify(10))  # => 10
​
​
### LOOPING
## For
todos = ["buy chips", "buy beer", "buy candles", "order pizza"]
for todo in todos:
    print(todo)