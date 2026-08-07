#question3
c=0
for i in range(1,11):
    if (i%2!=0):
        x=i*5
        print(i,'*','=',x)
    else:
        y=i+5
        print(i,'+','=',y)
        c+=y
        c+=x
    
print(c)
        