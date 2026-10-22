# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:00:07 2026

@author: Amirabas Ahmadi
"""
tasks = { 
    101: { 
        "id": 101, 
        "title": "Fix login bug", 
        "assignee": "Ali", 
        "priority": "HIGH", 
        "status": "OPEN" 
    }, 
    102: { 
        "id": 102, 
        "title": "Update API", 
        "assignee": "Sara", 
        "priority": "MEDIUM", 
        "status": "IN_PROGRESS" 
    }, 
    103: { 
        "id": 103, 
"title": "Write tests", 
"assignee": "Ali", 
"priority": "LOW", 
"status": "DONE" 
} 
} 
ALLOWED_TRANSITIONS = {
        "OPEN": {"IN_PROGRESS"},
        "IN_PROGRESS": {"DONE"},
        "DONE": set()
        }
    
priority_list=['LOW','MEDIUM',"HIGH"]
status_list=['OPEN','IN_PROGRESS','DONE']
class Task:
    def __init__(self,ids:int,title:str,assignee:str,priority:str,status:str):
        self.ids=ids
        self.title=title
        self.assignee=assignee
        self.priority=priority
        self.status=status
#------------Create---------------------
def Create_task(ids:int,title:str,assignee:str,priority:str,status:str):
    if ids in tasks:
        print('The requests already been sent.')
        return False
    priority=priority.upper()
    status=status.upper()
    if priority not in priority_list:
        print('The request is not in the priorities.')
        return False
    if status not in status_list:
        print('The request doesnt exist in the statuses.')
        return False
    else:
        tasks[ids]={
            'id':ids,
            'title':title,
            'assignee':assignee,
            'priority':priority,
            'status':status
            }
    return tasks
#-------------Read-----------
def Read_task(ids:int):
    if ids in tasks:
        return tasks[ids]
    else:
        print('The ID is invalid.')
        return False
#--------------Read All------------
def Read_all_tasks():
    if not tasks:
        print('No tasks available.')
        return
    for task_id, info in tasks.items():
        print(f"ID: {task_id} | Title: {info['title']} | Assignee: {info['assignee']} | Priority: {info['priority']} | Status: {info['status']}")
#------------Update---------    
#--------------Update------------
def Update_task(ids: int, title: str = None, assignee: str = None, priority: str = None):
    if ids not in tasks:
        print('The ID is invalid.')
        return False
    
    if title:
        tasks[ids]['title'] = title
    if assignee:
        tasks[ids]['assignee'] = assignee
    if priority:
        priority = priority.upper()
        if priority in priority_list:
            tasks[ids]['priority'] = priority
        else:
            print('The priority is invalid.')
            
    print('Task updated successfully.')
    return tasks[ids]


#--------------Change Status------------
def Change_status(ids: int, new_status: str):
    if ids not in tasks:
        print('The ID is invalid.')
        return False
    
    new_status = new_status.upper()
    if new_status not in status_list:
        print('The status is invalid.')
        return False
        
    current_status = tasks[ids]['status']
    allowed = ALLOWED_TRANSITIONS.get(current_status, set())
    
    if new_status not in allowed:
        print(f"Invalid transition from {current_status} to {new_status}.")
        return False
        
    tasks[ids]['status'] = new_status
    print(f"Status changed to {new_status} successfully.")
    return True


#--------------Delete------------
def Delete_task(ids: int, confirm: bool = False):
    if ids not in tasks:
        print('The ID is invalid.')
        return False
        
    current_status = tasks[ids]['status']
    if current_status in ['IN_PROGRESS', 'DONE'] and not confirm:
        print('Task is in progress or done. Confirmation required to delete.')
        return False
        
    del tasks[ids]
    print('Task deleted successfully.')
    return True


#--------------Filter & Search------------
def Filter_tasks(assignee: str = None, priority: str = None, status: str = None):
    results = []
    for info in tasks.values():
        match = True
        if assignee and info['assignee'].lower() != assignee.lower():
            match = False
        if priority and info['priority'].upper() != priority.upper():
            match = False
        if status and info['status'].upper() != status.upper():
            match = False
            
        if match:
            results.append(info)
            
    return results


#--------------Reports------------
def Generate_reports():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for info in tasks.values() if info['status'] == 'DONE')
    open_tasks = sum(1 for info in tasks.values() if info['status'] in ['OPEN', 'IN_PROGRESS'])
    
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Open tasks: {open_tasks}")
    
    assignee_open_count = {}
    for info in tasks.values():
        person = info['assignee']
        if info['status'] in ['OPEN', 'IN_PROGRESS']:
            assignee_open_count[person] = assignee_open_count.get(person, 0) + 1
            
    if assignee_open_count:
        busiest = max(assignee_open_count, key=assignee_open_count.get)
        print(f"Assignee with most open tasks: {busiest} ({assignee_open_count[busiest]} tasks)")


    
    
    
    
    
y=Read_all_tasks()