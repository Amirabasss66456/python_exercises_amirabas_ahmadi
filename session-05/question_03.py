s=input('enter your str:')
a=[' ']
b=['!','@','#','$','&']
alpha=0
upper=0
lower=0
digit=0
space=0
special=0
for i in s:
    if i.isalpha():
         alpha+=1
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
    if i.isdigit():
        digit+=1
    if i in a:
        space+=1
    if i in b:
        special+=1
print('Letters:',alpha)
print('Uppercase:',upper)
print('Lowercase:',lower)
print('Digits:',digit)
print('Spaces:',space)
print('Special characters:',special)