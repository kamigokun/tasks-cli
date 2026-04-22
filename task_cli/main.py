# main.py
# Entry point of the app.
# Reads what user types and calls the right command.

import sys
from task_cli.commands import (
    add_task,
    list_tasks,
    delete_task,
    update_task,
    mark_task
)


def show_usage():
    # Shows instructions when user types wrong command
    # or doesn't type anything at all
    print("""
Usage: python -m task_cli.main <command> [arguments]

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
    # sys.argv is everything the user typed as a list
    # Example: python -m task_cli.main add "Buy milk"
    # sys.argv = ["main.py", "add", "Buy milk"]

    # If user typed nothing, show instructions
    if len(sys.argv) < 2:
        show_usage()
        return

    # The command is always the second thing typed
    command = sys.argv[1]

    # --- ADD COMMAND ---
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python -m task_cli.main add <description>")
            return
        description = sys.argv[2]
        add_task(description)

    # --- LIST COMMAND ---
    elif command == "list":
        if len(sys.argv) == 3:
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()

    # --- DELETE COMMAND ---
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python -m task_cli.main delete <id>")
            return
        task_id = int(sys.argv[2])
        delete_task(task_id)

    # --- UPDATE COMMAND ---
    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python -m task_cli.main update <id> <description>")
            return
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        update_task(task_id, new_description)

    # --- MARK DONE COMMAND ---
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python -m task_cli.main mark-done <id>")
            return
        task_id = int(sys.argv[2])
        mark_task(task_id, "done")

    # --- MARK IN PROGRESS COMMAND ---
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python -m task_cli.main mark-in-progress <id>")
            return
        task_id = int(sys.argv[2])
        mark_task(task_id, "in-progress")

    # --- UNKNOWN COMMAND ---
    else:
        print(f"Error: Unknown command '{command}'")
        show_usage()


# Only run main() if this file is run directly
if __name__ == "__main__":
    main()