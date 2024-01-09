a=list(map(int,input().split()))
n=len(a)
ans=0
for i in range(n):
	ans += a[i]
print(ans-a[0])