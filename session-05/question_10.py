text1=input('type your text:')
text2=input('type your text2:')
f=text1.lower()
h=text2.lower()
a=f.split(' ')
b=h.split(' ')
print('Common words:')
for i in b:
    if i in a:
      print(i)