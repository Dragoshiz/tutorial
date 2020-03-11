import random
print("Vei incerca sa ghicesti numarul meu")
gen = random.randint(0,20)
guess = None

while guess != gen:
	guess = int(input("Alege un numar: "))
	if guess > gen:
		print("Mai jos")
	elif guess < gen:
		print("Mai sus")
print("Yuhuu!!!  Ai ghici")