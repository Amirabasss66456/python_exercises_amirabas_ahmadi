orders = [
('Ali', 'Laptop'),
('Sara', 'Phone'),
('Ali', 'Phone'),
('Reza', 'Laptop'),
('Sara', 'Laptop'),
('Ali', 'Tablet'),
('Reza', 'Phone')
]
a={}
for i, j in orders:
    if i in a:
        a[i].append(j)
    else:
        a[i] = [j]
print(a)