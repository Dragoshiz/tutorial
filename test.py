# print("Hello world")
# result=10/3
# print(result)
# result2 = str(10)
# # "10"
# print('Hello world')

# create first_name, last_name, age, location variables
# print a sentence like "I'm Dragos Imbre, 19 year old balbalba"

# greeting = "Hello"
# print(greeting + " there")

# first_name = "Imbrea"
# last_name = "Dragos"
# age = "24..25 minya bazdmeg"
# print (first_name + " " +last_name+ " "+ age)
# print("Hey, I'm {} {} and I'm {}".format(first_name, last_name, age))

def whoami(first_name, last_name, age):
	print("Hey, I'm {} {} and I'm {}".format(
		first_name,	last_name, age)
	)

def whomai_v2(person):
	print('hey im {} {} and Im {} from {}'.format(
		person['first_name'], person['last_name'], person['age'], person['location'])
	)
	for todo in person['todos']:
		print("have to do {}".format(todo))

dragos = {
	"first_name": "Dragos",
	"last_name" : "Imbrea",
	"age" : "24",
	"location" : 'kezdi',
	'todos': [
		'wake up',
		'drink',
		'fuck',
		'shit',
		'masturbate'
	]
}

Szeka = {
	"first_name": "Szeka",
	"last_name" : "Atti",
	"age" : "40",
	"location" : 'falusi',
	'todos': [
		'fuck',
	]
}


kriszta = {
	'first_name': "kriszta",
	'last_name': 'Fink',
	'age': '20',
	"location" : 'barot',
	'todos': [
		'porszivo',
		'porszivo',
		'porszivo'
	]
}



# print("Hey, I'm {} {} and I'm {}".format(
# 	dragos['first_name'], dragos['last_name'], dragos['age']))
# print(dragos)
# print("Hey, I'm {} {} and I'm {}".format(
# 	Szeka['first_name'], Szeka['last_name'], Szeka['age']))

# whoami(dragos['first_name'], dragos['last_name'], dragos['age'])
# whoami(Szeka['first_name'], Szeka['last_name'], Szeka['age'])

whomai_v2(person=dragos)
# whomai_v2(person=Szeka)
# whomai_v2(person=kriszta)


# todos = ['wake up', 'wash teeths', 'go to work']  # list
# mix = ['hello', 1000, 0.14]

# for todo in todos
# todos = ['wake up', 'wash teeths', 'go to work']  # list
# mix = ['hello', 1000, 0.14]

# for todo in todos:
# 	print('Have to do {}'.format(todo))

# print('todo: {}'.format(todo))

# print('First: {}'.format(todos[0]))
# print('Second: {}'.format(todos[1]))
# print('Third: {}'.format(todos[2]))
