inventory = {
'apple': 20,
'banana': 5,
'orange': 0,
'milk': 12,
'bread': 0
}
print('available:')
for i in inventory:
    f=inventory.get(i)
    if f>0:
     print(i,f)

print('Out of stock:')
for j in inventory:
    s=inventory.get(j)
    if s==0:
     print(j,s)