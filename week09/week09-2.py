a = [1 , 3 , 5, 7, 9]
for i in range(5):
  print("i是",i , "這時a[i]是", a[i])

print("比較好的寫法是 range(N)")

N = len(a)
for i in range(N):
  print("i是", i, "這時的a[i]的值是", a[i])