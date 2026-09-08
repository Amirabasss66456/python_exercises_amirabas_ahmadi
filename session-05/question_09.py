a='amir'
b='1386'

attempts=3
while attempts>0:
    user_name=input('Enter your username:')
    password=input('Enter password:')
    if a==user_name and b==password:
        print('Login successful')
        break
    else:
        attempts+=-1
        print('wrong username or password')
        print('attempts remaining:',attempts)
