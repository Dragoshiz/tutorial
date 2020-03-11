levels = int(input("How many levels do you want your fenyo?"))
star = "#"
blankspace = " "
lines = levels * blankspace + star
torzs = ((levels - 1) * blankspace + 2 *star)
for i in range(levels):
	num_stars = 2 * i + 1
	print(levels * blankspace + num_stars * star)
	levels= levels - 1
print(torzs)


