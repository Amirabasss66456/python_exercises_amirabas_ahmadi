file_users='C://Users//ayran//OneDrive//Desktop//python_exercises_amirabas_ahmadi//session-08//users.txt.txt'

def add_user(username, password, status):
    
    try:
        with open(file_users,'r') as f1:
            content=f1.readline()
    except:
        content=''
        
    if username not in content:
        with open(file_users,'a') as f1:
         f1.write(username+','+password+','+status)
         f1.write('\n')
         
add_user('ali','878767','active')
add_user('ali','drtdfd','block')
def find_user(username):
    try:
        with open(file_users,'r') as f1:
            for line in f1:
                parts=line.strip().split(',')
                if parts[0]==username:
                  print('user found',line.strip())
                else:
                     print('user not found')
    except:
        pass
def delete_user(username):
    with open(file_users,'r')as f1:
        lines=f1.readlines()
        
    new_lines=[]
    user_found=False
    
    for line in lines:
        parts=line.strip().split(',')
        if parts[0]==username:
            user_found=True
        else:
            new_lines.append(line)
    if user_found:
        with open(file_users,'w') as f1:
            for line in new_lines:
                f1.write(line)
        print('user deleted')
    else:
        print('user not found')
def generate_report():
    active_count = 0
    blocked_count = 0

    try:
        with open(file_users, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    status = parts[2].strip()
                    if status == 'active':
                        active_count += 1
                    elif status == 'blocked':
                        blocked_count += 1
    except:
        pass

    print("Active users:", active_count)
    print("Blocked users:", blocked_count)
generate_report()
            
                
