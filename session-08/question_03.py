transactions_file='C://Users//ayran//OneDrive//Desktop//python_exercises_amirabas_ahmadi//session-08//transactions.txt.txt'
def total_deposits():
    deposits={}
    with open(transactions_file,'r') as f1:
        for line in f1:
            line=line.strip()
            if not line:
                continue
            user,action,amount=line.split(',')
            amount=int(amount)
            if action=='deposit':
                deposits[user]=deposits.get(user,0)+amount
            return deposits
def total_withdrawals():
    balances={}
    valid_withdrawals={}
    with open(transactions_file,'r') as f1:
        for line in f1:
            line=line.strip()
            if not line:
                continue
            user,action,amount =line.split(',')
            amount=int(amount)
            if user not in balances:
                balances[user]=0
                valid_withdrawals[user]=0
            if action=='deposit':
                balances[user]+=amount
            elif action=='withdraw':
                if amount<=balances[user]:
                    balances[user]-=amount
                    valid_withdrawals[user]+=amount
    return valid_withdrawals
def calculate_balance():
    balances = {}
    with open(transactions_file, "r") as f1:
        for line in f1:
            line = line.strip()
            if not line:
                continue
            user, action, amount = line.split(",")
            amount = int(amount)
            if user not in balances:
                balances[user] = 0
            if action == "deposit":
                balances[user] += amount
            elif action == "withdraw":
                if amount <= balances[user]:  
                    balances[user] -= amount
    return balances

def find_invalid_transactions():
    balances = {}
    invalid_transactions = {}
    with open(transactions_file, "r") as f1:
        for line in f1:
            line = line.strip()
            if not line:
                continue
            user, action, amount = line.split(",")
            amount = int(amount)
            if user not in balances:
                balances[user] = 0
                invalid_transactions[user] = []
            if action == "deposit":
                balances[user] += amount
            elif action == "withdraw":
                if amount > balances[user]:
                    invalid_transactions[user].append((action, amount))
                else:
                    balances[user] -= amount
    return invalid_transactions

def generate_report():
    deposits = total_deposits()
    withdrawals = total_withdrawals()
    balances = calculate_balance()
    invalids = find_invalid_transactions()
    all_users = set(deposits.keys()) | set(balances.keys())
    print("--- Users' financial transaction report ---\n")
    for user in all_users:
        print(f"Username: {user}")
        print(f"  - Total deposit: {deposits.get(user, 0):,}")
        print(f"  - Total valid withdrawals: {withdrawals.get(user, 0):,}")
        print(f"  - Final inventory: {balances.get(user, 0):,}")

        user_invalids = invalids.get(user, [])
        if user_invalids:
            print(f"  - Invalid transactions: {user_invalids}")
        else:
            print("  - Invalid transactions: None")
        print("-" * 35)

generate_report()

    
            
                