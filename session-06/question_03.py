a=input("enter str:")
d={}
for i in a:
    if i.isalpha():
      if i in d:
         d[i]+=1
      elif i not in d:
        d[i]=1
print(d)