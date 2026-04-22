import sys
from task_cli.commands import(
    add_task,
    list_tasks,
    delete_task,
    update_task,
    mark_task
)


def show_usage():
    # This prints instructions when user types wrong command
    # or doesn't type anything at all
    print("""
Usage: python main.py <command> [arguments]

Commands:
  add <description>              Add a new task
  list                           List all tasks
  list done                      List completed tasks
  list todo                      List pending tasks
  list in-progress               List in-progress tasks
  update <id> <description>      Update a task
  delete <id>                    Delete a task
  mark-done <id>                 Mark task as done
  mark-in-progress <id>          Mark task as in progress
    """) 


def main():
    # sys.argv is a list of everything the user typed
    sys.argv = ["main.py", "add", "Buy milk"]

    # If user typed nothing except the file name then show instruction
    if len(sys.argv)<2:
        show_usage
        return
    
    # The command is always the second thing typed
    command = sys.argv[1]


    #===== ADD COMMAND =====
    if command == "add":
        # Make sure they also typed a description
        if len(sys.argv)<3:
            print("Usage: python main.py add <description>")
            return
        
        # Everything after "add" is the description
        description = sys.argv[2]
        add_task(description)

    # =====LIST COMMAND=====
    elif command == "list":
        # Check if they typed a status filter like "done" or "todo"
        if len(sys.argv) == 3:
            status = sys.argv[2]
            list_tasks(status)
        else:
            # No filter = show all tasks 
            list_tasks()

    # ===== DELETE COMMAND=====
    elif command == "delete":
        # Make sure they typed an ID 
        if len(sys.argv) <3:
            print("Usage: python main.py delete <id>")
            return
        # Convert the ID from string to integer
        task_id = int(sys.argv[2])
        delete_task(task_id)


    # =====UPDATE COMMAND======
    elif command == "update":
        # Make sure they typed both ID and new description
        if len(sys.argv) < 4 :
            print("Usage: python main.py update <id> <description>")
            return
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        update_task(task_id, new_description)



    # ======MARK DONE COMMAND======
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-done <id>")
            return
        task_id = int(sys.argv[2])
        # Pass "done" as the status to mark_task
        mark_task(task_id, "done")



    # ======MARK IN PROGRESS COMMAND========
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-in-progress <id>")
            return
        task_id = int(sys.argv[2])
        # Pass "in-progress" as the status to mark_task
        mark_task(task_id, "in-progress")


    # ======UNKNOWN COMMAND======
    else:
        print(f"Error: Unknown command '{command}")
        show_usage()

# "Only run main() if this file is run directly"
# Not when it's imported by another file
if __name__ == "__main__":
    main()
