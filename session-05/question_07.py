s=input('enter your str:')
a=''
b=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        b+=1
    else:
        a+= s[i]+str(b)
        b=1
a+=s[-1]+str(b)
print(a)