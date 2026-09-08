s=input('Enter your text:')
a=s.lower()
b=a.split(' ')
h=['hack','fraud','scam','password','attack']
for i in h:
    if i in b:
        print(i,'->',b.count(i))