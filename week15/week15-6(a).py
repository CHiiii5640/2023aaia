x1,y1,x2,y2=map(int,input().split())

ans=(x2-x1)*(y2-y1)
if ans<0:
	ans=-ans
print( ans ,end="")