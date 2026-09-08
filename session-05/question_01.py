password=input("enter your password:")
speciall=['@','$','&',"!"]
alpha=False
upper=False
lower=False
digit=False
special=False
for i in password:
    if i.isalpha():
        alpha=True
    if i.isupper():
        upper=True
    if i.islower():
        lower=True
    if i.isdigit():
        digit=True
    if i in speciall:
            special=True
ok=True
if len(password)<8:
    print('password is invalid')
    print("password password must contain at least 8 characters")
    ok=False
if not alpha:
        print('password is invalid')
        print('password must contain a alpha character')
        ok=False
if not upper:
        print('password is invalid')
        print('password must contain a upper character')
        ok=False
if not lower:
        print('password is invalid')
        print('password must contain a lower character')
        ok=False
if not digit:
            print('password is invalid')
            print('password must contain a digit character')
            ok=False
if not special:
            print('password is invalid')
            print('password must contain a special character')
            ok=False
if ok:
      print('password successfully created')
    
        
