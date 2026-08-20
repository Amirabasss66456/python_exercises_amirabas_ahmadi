a=input('لطفا رمز عبور را وارد نمایید:')
if len(a)==8 and a[4:].isdigit()==True and a[:4].isalpha()==True :
        print('معتبر.')
else:
        print('نامعتبر.')
    

