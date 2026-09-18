users = [
    ("Ali", 25, "Python"),
    ("Sara", 30, "Java"),
    ("Reza", 22, "Python"),
    ("Mina", 28, "C++"),
    ("John", 35, "Python"),
    ("David", 30, "Java"),
]
a={}
for i,j,x in users:
    if x in a:
        a[x].append(i)
    else:
        a[x] = [i]
print(a)