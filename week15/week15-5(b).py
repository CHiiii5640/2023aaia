a=int(input())
if a==0:
	print("0")
if a<0:
	a=str(a)
	print(a[1])
else:
	a=str(a)
	print(a[0])