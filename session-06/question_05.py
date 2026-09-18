students = {
'Ali': [18, 17, 20],
'Sara': [15, 19, 18],
'Reza': [12, 14, 10],
'Mina': [20, 20, 19] }
avg=15
f=0
for i in students['Ali']:
    f+=i/len(students['Ali'])
print('Ali')
print('avg:',f)
if f>=15:
    print('status:passed')
else:
    print('status:failed')
h=0
for j in students['Sara']:
    h+=j/len(students['Sara'])
print('Sara')
print('avg:',h)
if h>=15:
    print('status:passed')
else:
    print('status:failed')
l=0
for x in students['Reza']:
    l+=x/len(students['Reza'])
print('Reza')
print('avg:',l)
if l>=15:
    print('status:passed')
else:
    print('status:failed')
p=0
for y in students['Mina']:
    p+=y/len(students['Mina'])
print('Mina')
print('avg:',p)
if p>=15:
    print('status:passed')
else:
    print('status:failed')
s=[f,h,l,p]
print('best student:Sara',max(s))
