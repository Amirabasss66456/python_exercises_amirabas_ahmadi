string=input('enter your string:')
s=''
for i in string:
    if i not in s:
        s+=i

print(s)