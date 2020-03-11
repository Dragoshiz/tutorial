from sys import argv

script, user_name, faszod = argv
prompt = '-'

print("Hi {}, I'm the {} script. Nagy faszu allat {}".format(user_name, script, faszod))
print("I'd like to ask you a few questions.")

print("Do you like me {}".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {} about liking me.
You live in {}. Not sure where you at nigga.
And you have a shitty ass {} computer. That's fucked up nigga
Yo dick {} big!? """.format(likes, lives, computer, faszod))