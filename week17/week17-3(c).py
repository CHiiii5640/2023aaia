a=input()

if a.isalpha():
    if a.isupper():
        print('U', end='')
    if a.islower():
        print('L', end='')
elif a.isdigit():
    print('D', end='')
else:
    print('O', end='')