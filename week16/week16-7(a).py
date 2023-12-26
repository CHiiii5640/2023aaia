a=list(map(int,input().split()))

a.sort()
x=int(str(a[-1]))
y=int(str(a[-2]))
z=int(str(a[-3]))
print(f'{x*100+y*10+z+1}',end="")