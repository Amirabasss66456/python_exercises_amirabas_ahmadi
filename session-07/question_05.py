def analyze_logs(logs):
    successful_logins = 0
    failed_logins = 0
    user_actions = {}
    user_403_counts = {}

    for username, action, status in logs:
        if action == "LOGIN":
            if status == 200:
                successful_logins += 1
            else:
                failed_logins += 1

        if status == 403:
            user_403_counts[username] = user_403_counts.get(username, 0) + 1

        user_actions[username] = user_actions.get(username, 0) + 1

    suspicious_users = [user for user, count in user_403_counts.items() if count >= 3]

    report = {
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "suspicious_users": suspicious_users,
        "user_action_counts": user_actions
    }

    return report


logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403)
]

result = analyze_logs(logs)
print(result)