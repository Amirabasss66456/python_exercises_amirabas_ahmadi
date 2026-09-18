employees = {
'E01': {
'name': 'Ali',
'age': 28,
'salary': 3000
},
'E02': {
'name': 'Sara',
'age': 32,
'salary': 4500
},
'E03': {
'name': 'Reza',
'age': 25,
'salary': 2800
}
}
a=0
b=''
for i in employees.values():
    if i['salary']>a:
        a=i['salary']
        b=i['name']
print('name:',b)
print('max salary:',a)

f=0
for j in employees.values():
        f+=j['salary']/len(employees)
print('avg:',f)

for x in employees.values():
    if x['salary']>3000:
        print(x)

c=float('inf')
d=''
for y in employees.values():
    if y['salary']<c:
        c=y['salary']
        d=y['name']
print('min salary:',d)
