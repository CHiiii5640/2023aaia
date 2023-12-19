def gcd(a,b):
	while b!=0:
		a,b=b,a%b
	return a
a,b=map(int,input().split())
result=gcd(a,b)
print('Enter two integers: ')
print(f'The greatest common divisor of {a} and {b} is {result}')