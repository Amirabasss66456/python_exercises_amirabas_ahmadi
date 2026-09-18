sales = (
('Ali', 'Laptop', 1200),
('Sara', 'Phone', 800),
('Ali', 'Phone', 800),
('Reza', 'Laptop', 1200),
('Sara', 'Laptop', 1200),
('Ali', 'Mouse', 50)
)
a = {}
b = {}
c = 0
for i, j, x in sales:
    if i in a:
        a[i]+=x
    else:
        a[i]=x
    if j in b:
        b[j]+=1
    else:
        b[j]=1
    c+=x

f=max(a, key=a.get)

print("میزان خرید هر مشتری:", a)
print("مشتری با بیشترین خرید:", f)
print("تعداد فروش هر محصول:", b)
print("مجموع درآمد فروشگاه:", c)