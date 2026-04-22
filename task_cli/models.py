# This file defines what a task looks like
# and how to create or validate one

from datetime import datetime

# The only 3 valid statuses a task can have
VALID_STATUSES = ["todo", "in-progress", "done"]


def create_task(task_id, description):
    # Get current time as a string 
    now = datetime.now().isoformat()

    # Return a dictionary with all 5 required fields 
    return {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
  
def validate_description(description):

    # Check if description is empty or just whitespaces
    if not description or not description.strip():
        return False, "Error: Task description cannot by empty."
    # Check if description is too long
    if len(description) > 200:
        return False, "Error: Description too long (max 200 characters)."
    
    # All good 
    return True, None