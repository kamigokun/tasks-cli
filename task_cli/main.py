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