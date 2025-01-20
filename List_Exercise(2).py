

to_do=[]

def add_tasks():
    add_task=input("Please Enter the task you want to add to your list: ")
    to_do.append(add_task)
    return add_task

def remove_tasks():
    print(f"{to_do} This is your current tasks!")
    remove_task=input("Which task would you like to remove: ")
    if remove_task not in to_do:
        print("This Task is not in your list!")
    else:
        to_do.remove(remove_task)
        return remove_task
    
def view_task():
    print(f"{to_do} these are all your tasks!")
    
def completed_task():
    print(f"{to_do} This is your current tasks!")
    task_complete=input("Which of these tasks you want to mark as completed: ")
    if task_complete in to_do:
        to_do.remove(task_complete)
        to_do.append(f"{task_complete} (completed)")
        print(f"{task_complete} task is marked as completed!")
        return task_complete
    else:
        print("This task is not in your list!")
        return None
    
    
while True:
    system_=input("Welcome to the To-Do List Manager!\n"
                  "1-Add Task \n"
                  "2-Remove Task \n"
                  "3- View Task \n"
                  "4- Mark Task as Completed \n"
                  "5-Exit \n"
                  
                  ).lower()
    
    if system_ == "1":
        task_add=add_tasks()
        print(f"{task_add} added to your tasks list!")
        
    elif system_ =="2":
        task_remove=remove_tasks()
        print(f"{task_remove} has been removed from your tasks list!")
        
    elif system_ == "3":
        view_task()
        
    elif system_== "4":
        completed_task()
        
    elif system_ == "5":
        print("Program Terminated!")
        break