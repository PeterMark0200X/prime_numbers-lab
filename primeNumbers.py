import math

def genPrimes(n):
	for i in range(2, int(math.sqrt(n)+1)):
		if n % i == 0: 
			return False;
	return n>1;
	
num = int(input('enter the maximum range eg"100/300"; '))
prime = []

def primeNumbers(num):
	if num <= 0:
		return prime
	else:
		for n in range (num):
			if genPrimes(n):
				prime.append(n)
		return prime
		

