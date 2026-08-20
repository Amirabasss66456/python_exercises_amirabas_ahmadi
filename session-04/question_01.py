import random
c=random.randint(1,10)
while True:
    a=int(input('عدد خود را وارد نمایید:'))
    if c<a:
        print('عدد را کوچکتر کن')
    elif c>a:
        print('عدد را بزرگتر کن')
    else:
        print('تبریک.شما موفق به پیدا کردن عدد شدید.')
        break
        
    