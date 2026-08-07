a=int(input('موجودی حساب خود را وارد نمایید:'))
b=int(input('مبلغ برداشت زا وارد نمایید:'))
if b>0:
    if a>=b:
        print(a-b)
    else:
        print('موجودی ناکافی')
elif b<=0:
    print('خطا!!!!')