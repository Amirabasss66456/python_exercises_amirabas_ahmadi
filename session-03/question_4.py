#question4
a=input('enter string:')
c=0
for i in a:
    c+=1
s=c // 2
if c %2!=0:
    print(a[s:])
elif c%2!=5:
    print(a[:s])
    