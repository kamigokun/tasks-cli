from task_cli.storage import load_tasks, save_tasks, get_next_id, find_task_by_id  
from task_cli.models import create_task, validate_description, VALID_STATUSES
from datetime import datetime



def add_task(description):
    # step 1: validate before doing anything
    is_valid, error = validate_description(description)
    if not is_valid:
        print(error)
        return
    
    # step 2: load existing tasks 
    tasks= load_tasks()

    # step 3: figure out the next ID 
    new_id = get_next_id(tasks)

    # step 4 : create the task using our model 
    task = create_task(new_id, description)

    # step 5: add it to the list 
    tasks.append(task)

    # step 6: save the updated list 
    save_tasks(tasks)


    print(f"Task added successfully (ID: {new_id})")



def list_tasks(status=None):
    tasks = load_tasks()

    # Filter by status if one was provided
    if status:
        if status not in VALID_STATUSES:
            print(f"Error: Invalid status '{status}'. Choose from : {VALID_STATUSES}")
            return 
        tasks = [task for task in tasks if task["status"] == status]
    # Handle empty results
    if not tasks:
        print(f"No tasks found.")
        return
    
    # Print each task in a readable format
    print(f"/n{'ID' : <5} {'Status':<15} {'Description'}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5} {task['status']:<15} {task['description']}")
    print()



def delete_task(task_id):
    tasks = load_tasks()

    # Check if task exists
    task = find_task_by_id(tasks,task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    # Remove it from the list
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id}  deleted successfully.")




def update_task(task_id, new_description):
    # Validate the new description first
    is_valid, error = validate_description(new_description)


    # If description is bad, show error and stop immediately
    if not is_valid:
        print(error)
        return 
    
    # Load all tasks from task.json as a python list
    tasks = load_tasks()

    task = find_task_by_id(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    # Replace the old description with the new one
    task["description"] = new_description

    task["updateAt"] = datetime.now().isoformat()

    save_tasks(tasks)

    print(f"Task {task_id} updated successfully")




def mark_task(task_id, status):

    # Check if the status is one of the 3 valid options
    if status not in VALID_STATUSES:
        print(f"Error: '{status}' is not a valid status.")
        print(f"Valid options are: {VALID_STATUSES}")
        return
    tasks = load_tasks()

    task = find_task_by_id(tasks, task_id)
    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return
    # Replace the old status with the new one
    task["status"] = status
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {task_id} marked as '{status}' successfully")