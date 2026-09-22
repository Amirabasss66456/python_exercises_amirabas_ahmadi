text1=input('Enter your text:')
def  analyze_text(text):
    letter=0
    digit=0
    most_common_letter=text.replace(' ','')
    Palindrome=0
    uppercase=0
    lowercase=0
    text2=text.split()

    for char in text:
        if char.isalpha()==True:
            letter+=1
        if char.isdigit()==True:
            digit+=1
        if char.isupper()==True:
            uppercase+=1
        if char.islower()==True:
            lowercase+=1
    most_common_char = max(most_common_letter, key=most_common_letter.count)
    count = most_common_letter.count(most_common_char)

    for char in text2:
         if text[::-1]==text:
             Palindrome+=1
    most_common_word = max(text2, key=text2.count)
    count = text2.count(most_common_word)
    result={
    'words:':len(text2),
    'letters:':letter,
    'digits:':digit,
    'most_common_letter:':most_common_char,
    'uppercase:':uppercase,
    'lowercase:':lowercase,
    'most_common_word:':most_common_word,    
    'longest_word:':max(text2,key=len),
    'shortest_word:':min(text2,key=len),
    'palindrome_words:':Palindrome,
    }         
    return result
            

output=analyze_text(text1)
print(output)