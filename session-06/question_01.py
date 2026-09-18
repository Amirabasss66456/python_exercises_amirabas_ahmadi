products= {
'laptop': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}
bozorg=max(products,key=products.get)
kochak=min(products, key=products.get)
print('max','=',bozorg)
print('min','=',kochak)
f=0
for i in products:
    s=products.get(i)
    f+=s
    
print('avg','=',f/len(products))
for i in products:
    if products.get(i)>500:
        print(i)
for i in products:
    s=products.get(i)
    f+=s
print(f)