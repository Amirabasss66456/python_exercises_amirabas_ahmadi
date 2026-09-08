s=input('enter your text:')
print('Total characters:',len(s))
a=s.split(" ")
b=[" "]
h=''
short=a[0]
most_characters=s[0]
most_character=s.count(s[0])
most_words=a[0]
most_word=a.count(a[0])
alpha=0
digit=0
space=0
uppers=0
lowers=0
for i in s:
    if i.isalpha():
       alpha+=1 
    if i.isdigit():
        digit+=1
    if i in b:
        space+=1
    if i.isupper():
        uppers+=1
    if i.islower():
        lowers+=1
    if s.count(i)>most_character:
        most_character=s.count(i)
        most_characters=i
print('Total letters:',alpha)
print('Total digits:',digit)
print('Total spaces:',space)
print('Total uppercase:',uppers)
print('Total lowercase:',lowers)

for i in a:

    if len(i)>len(h):
        h=i
    if len(i)<len(short):
        short=i
    if a.count(i)>most_word:
        most_word=a.count(i)
        most_words=i
print('Total words:',len(a))
print('Longest word:',h)
print('Shortest word:',short)
print('Most repeated character:',most_characters)
print('Most repeated word:',most_words)