a = 150000000 #老大
b = 200000000 #老二
c = a%b    #老三
print(a,b,c)
while c!=0: #輾轉相除法
  a = b #老二變老大
  b = c #老三變老二
  c = a%b #新的老三
  print(a,b,c)
print(b)