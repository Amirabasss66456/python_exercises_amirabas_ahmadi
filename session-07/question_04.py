def detect_fraud(transactions):
    suspicious_transactions = []
    
    balances = {}
    consecutive_withdraws = {}

    for tx in transactions:
        username, tx_type, amount, time = tx
        
        if username not in balances:
            balances[username] = 0
            consecutive_withdraws[username] = 0

        is_suspicious = False

        if amount > 100000000:
            is_suspicious = True

        if tx_type == "withdraw":
            if amount > balances[username]:
                is_suspicious = True

            consecutive_withdraws[username] += 1

            if consecutive_withdraws[username] > 3:
                is_suspicious = True

            balances[username] -= amount

        elif tx_type == "deposit":
            consecutive_withdraws[username] = 0
            balances[username] += amount

        if is_suspicious:
            suspicious_transactions.append(tx)

    return suspicious_transactions


transactions = [
    ("Ali", "deposit", 50000000, 10),
    ("Ali", "withdraw", 2000000, 11),
    ("Ali", "withdraw", 3000000, 12),
    ("Ali", "withdraw", 4000000, 13),
    ("Ali", "withdraw", 5000000, 14),
    ("Ali", "withdraw", 6000000, 15),
    ("Sara", "deposit", 50000000, 20),
    ("Sara", "withdraw", 60000000, 21),
    ("Reza", "deposit", 150000000, 30)
]

result = detect_fraud(transactions)
print(result)