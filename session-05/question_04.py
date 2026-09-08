s=input('enter your sentence:')
c=''
h=0
a=s.lower()
b=a.split(" ")
for i in b:
    if b.count(i)>h:
        h= b.count(i)
        c=i
print(c,'->' ,h)