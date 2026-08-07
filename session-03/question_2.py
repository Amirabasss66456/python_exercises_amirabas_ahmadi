#question2
c=0
for i in range(1,11):
    a=float(input('رکورد پرش خود را ثبت کنید:'))
    
    if a<c:
     print('این مقدار قبلا ثبت شده است')
    else:
        
        c=a
        print('رکورد تازه ای ثبت شده است')
        print(c,'بیشترین پرش تا این لحظه ثبت شد.') 
        
         


