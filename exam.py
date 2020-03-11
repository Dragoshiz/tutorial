import subprocess
import pprint

"""
1. Write variables one with:
	- a string
	- an int
	- a float
	- a boolean
	- a list
	- a dict

2. Write functions which,
	- prints Hello to the screen
	- return "Hello" to a variable then print the variable
	- takes a number argument and adds 2 to it -> print the result
	- takes a number and adds 2 to it -> returns the value to a variable

3. Write an if/elif/else statement for a random number

4. Generate 10 radom number and create a for loop to print them one-by-one

5. !!! Find a way to store information about a school. It should
   contain the followings:
	- name
	- description
	- Teachers (add atleast 2)
		- first_name, last_name, age, tantargy
	- director
		- first_name, last_name, age, tantargy


"""

# 1- variables:
# myname = str("Imbrea Dragos")
# numint =  int(4 + 5.9)
# numfl = float(3.54 - 2.76)
# boolean = 4 < 3 
# shopping_list = ['cotet', 'meg egy cotetot', 'stb']
# dis_dict ={
# 	"anal": "good",
# 	"suck": "almost as good",
# 	"anyad szuletett" : 1955
# 	}
# print(myname, numint, numfl, boolean, shopping_list, dis_dict)

# 2- Function
# def var(hi):
# 	hi = "This fuction just fucking says fucking {}".format(hi)
# 	return hi

# baszott_variable = var("hello")

# print(var("hello"))
# 

# import random

# gen = (random.randint(0,10))

# if gen < 5:2
# 	print("kissebb te fasz")
# elif gen > 5:
	# print(" nagybb szopjal gecit te gecilada faszzopo ")
# else:
# 	print("anyad")

# import random

# for x in range(10):
# 	gen = (random.randint(0,10))
# 	print(gen)

name= "gabor_aron"
description = "egy szar iskola"
teachers = {
			'szekely_attila':{
			'age : 69',
			'tantargy : sexology'},
			'Csoves Leszek':{
			'age : holnap',
			'tantargy :Apad'},
}
director = {
			'imbrea_dragos'
			'age : 20',
			'tantargy : anyad0'
}

iskola = {
	'name': name,
	'description' : description, 
	'teachers' : teachers, 
	'director' :director
}
pp = pprint.PrettyPrinter(indent=4)


pp.pprint(iskola)

fasz = input('lesz vizsga? :')
if fasz == 'nem':
	print('anyad')
elif fasz == 'igen':
	print('anyad')

subprocess.call(['shutdown -h now'])