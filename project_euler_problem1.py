#Matthew Violet 
#December 15 2015

total = 0

for num in range(1000):
	if (num % 3 == 0) or (num % 5 == 0):
		total = total + num

print(total)