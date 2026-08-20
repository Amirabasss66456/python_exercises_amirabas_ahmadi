import random
b=['سنگ','کاغذ','قیچی']
while True:
    a=input('لطفا سنگ,کاغذ و یا قیچی را وارد نمایید:')
    if a=='exit':
       break
    if a not in b:
      print("دوباره وارد کنید:")
      continue
    c=random.choice(b)
    print("انتخاب کامپوتر",':',c)
    if a=="سنگ"and c=='کاغذ':
            print('شما باختید.')
    elif a=='کاغذ'and c=='سنگ':
            print('شما بردید.')
    elif a=='قیچی' and c=='کاغذ':
            print('شما بردید.')
    elif a=='کاغذ'and c=="قیچی":
            print('شما باختید.')
    elif a=='سنگ'and c=='قیچی':
            print('شما بردید.')
    elif a=='قیچی'and c=='سنگ':
            print('شما باختید.')
    elif a==c:
            print("مساوی شدید.")
         
