a = int(input())

good = 0
if a%400==0: good = 1
elif a%100==0: good = 0
elif a%4==0: good = 1
else: good = 0

if good==1: print(a, 'is a leap year.')
else: print(a, 'is not a leap year.')