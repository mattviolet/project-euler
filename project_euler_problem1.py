#Matthew Violet 
#December 15 2015

total = 0

for num in range(1000):
	if (num % 3 == 0) or (num % 5 == 0):
		total = total + num

print("The sum of all numbers below 1000 that are divisible by 3 and 5 is: " + str(total))