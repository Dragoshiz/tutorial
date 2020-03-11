# RETURN


def whoami(first_name, last_name, age):
	print("Hey, I'm {} {} and I'm {}".format(
		first_name,	last_name, age)
	)

def whomai_v2(person):
	result = 'hey im {} {} and Im {} from {}'.format(
		person['first_name'], person['last_name'], person['age'], person['location'])
	return result

def get_todos_count(person):
	"""Returns todos count"""
	return len(person['todos'])


# function which takes a name, age, location, and todos
def build_person_dict(name, age, location, todos):
	name = name.split()
	person = {
		'first_name': name[0],
		'last_name': name[1],
		'age': age,
		'location': location,
		'todos': todos,
	}
	return person
# ad returns a person dictionary


atesz = build_person_dict(name='Sylveszter Atesz', age=35, location='Mili', todos=['semmi'])
print(whomai_v2(atesz))

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


eredmeny = whomai_v2(Szeka)
szeka_todos_count = get_todos_count(Szeka)
if szeka_todos_count <= 1:
	print('Easy')
elif szeka_todos_count > 1 and szeka_todos_count < 3:
	print('Go to work')
else:
	print('Fuck off Dragos')