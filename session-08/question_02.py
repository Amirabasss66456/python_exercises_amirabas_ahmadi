logs_file='C://Users//ayran//OneDrive//Desktop//python_exercises_amirabas_ahmadi//session-08//logs.txt.txt'
def count_successful_logins():
    successful=0
    with open(logs_file,'r') as f1:
        for line in f1:
            user,action,status=line.strip().split(',')
            if action=='LOGIN'and status=='200':
                successful+=1
    return successful

def count_failed_logins():
    failed=0
    with open(logs_file,'r') as f1:
        for line in f1:
            user,action,status=line.strip().split(',')
            if action=='LOGIN' and status!='200':
                failed+=1
    return failed
            
def find_suspicious_users():
    error_403_counts={}
    with open(logs_file,'r') as f1:
        for line in f1:
            user,action,status=line.strip().split(',')
            if status=='403':
                error_403_counts[user]=error_403_counts.get(user,0)+1
    suspicious = [user for user, count in error_403_counts.items() if count >= 3]
    return suspicious
                
def count_user_activities():
    user_counts = {}
    with open(logs_file, 'r') as f1:
        for line in f1:
            user, action, status = line.strip().split(',')
            user_counts[user] = user_counts.get(user, 0) + 1 
    return user_counts


def generate_report():
    successful = count_successful_logins()
    failed = count_failed_logins()
    suspicious = find_suspicious_users()
    user_activities = count_user_activities()
    
    print("--- Final system report ---")
    print("successful logins:", successful)
    print("failed logins:", failed)
    print("suspicious users:", suspicious)
    print('user activities:')
    for user, count in user_activities.items():
        print(f" {user}: {count} ")






generate_report()