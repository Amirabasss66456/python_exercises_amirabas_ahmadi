transactions = [
    ("Ali", "deposit", 5000000),
    ("Ali", "withdraw", 1000000),
    ("Sara", "deposit", 8000000),
    ("Ali", "withdraw", 500000),
    ("Sara", "withdraw", 2000000),
    ("Reza", "deposit", 10000000)
]
def analyze_transactions(transactions):
    result={}
    for name,ty,amount in transactions:
        if name not in result:
            result[name] = {
                'Deposit':0,
                'withdraw':0,
                'Balance change':0,
                'Number of Transactions':0
           }
        result[name]['Number of Transactions']+=1
        if ty=='deposit':
            result[name]['Deposit']+=amount
        elif ty=='withdraw':
            result[name]['withdraw']+=amount
    for name in result:
        result[name]['Balance change']= result[name]['Deposit']-result[name]['withdraw']
    return result

a=analyze_transactions(transactions)
print(a)