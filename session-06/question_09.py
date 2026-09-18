products = {
    "P01": ("Laptop", 1200, 5),
    "P02": ("Phone", 800, 0),
    "P03": ("Tablet", 500, 12),
    "P04": ("Mouse", 50, 25),
    "P05": ("Keyboard", 100, 0),
}
a=[]
b=[]
c={}
f= 0
for i, (name, price, stock) in products.items():
    if stock > 0:
        a.append(name)
    else:
        b.append(name)
    value = price * stock
    c[name] = value
    f+= value
h=max(c, key=c.get)
print("محصولات موجود:", a)
print("محصولات ناموجود:", b)
print("ارزش کل موجودی هر محصول:", c)
print("محصول با بیشترین ارزش موجودی:", h)
print("ارزش کل انبار:", f)