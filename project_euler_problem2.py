##Matthew Violet
##December 2015



def fib(x):
	if x == 1 or x == 2:
		return 1
	return fib(x-1) + fib(x-2)
	

total = 0

for i in range(33, 0, -1):
	val = fib(i)
	if val % 2 == 0:
		total = total + val
	


print(total)
