a=int(input())
ans=0
for i in range(11,a*11+1):
	if i%11==0:
		ans += i
print(ans,end="")