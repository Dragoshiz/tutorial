"""
Write a function which calculates the first N (function parameter) fi-
bonacci numbers.

NOTE: The first 2 fibonacci numbers are 0 and 1 and the next is the sum
of the previous 2 (for ex.: the third is 0 + 1 = 1). Your function 
should print N fibonacci number

EXTRA: After solving this by your own, google "python fibonacci recursion
solution" to see the result with a different approach. (recursion)
"""
def fib_num_count():
	num_count = int(input("Enter Fibonacci numbers lenght: "))
	if num_count == 1 :
		result = [0]

	elif num_count == 2 :
		result = [0,1]
	else:

		result = [0,1]
		additional_steps = num_count -2 
		for i in range(additional_steps):
			new_number = result[-1] + result[-2]
			result.append(new_number)
	return result

res = fib_num_count()
print(res)
