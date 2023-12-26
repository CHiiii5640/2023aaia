a=list(map(int,input().split()))
n=len(a)
if max(a)-min(a)==max(a):
	print(n-1,end="")