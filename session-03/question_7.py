a=input("Enter your like color:")
b=input("Enter your like color2:")
c=input('Enter your like color3:')
if a==b==c:
    print('سه رنگ یکسان هستند')
elif a==c:
    print('دو رنگ یکسان هستند ')
elif b==c:
    print('دو رنگ یکسان هستند')
elif b==a:
    print("دو رنگ یکسان هستند")
else:
    print('رنگ ها یکسان نیستند')