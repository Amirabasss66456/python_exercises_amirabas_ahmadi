s=input('enter your sentence:')
a=s.lower()
b=a.split(" ")
h=""
for i in b:
    if len(i)>len(h):
        h=i
print(h)
print('Lenghth:',len(h))