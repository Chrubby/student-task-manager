"""Core task-management functions. Kept separate from the UI for easy testing."""

import json
from pathlib import Path
from uuid import uuid4

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks(file_path=DATA_FILE):
    """Load tasks from a JSON file. Return an empty list if it does not exist."""
    path = Path(file_path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks, file_path=DATA_FILE):
    """Save the task list to a JSON file."""
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(tasks, course, name, due_date, priority, file_path=DATA_FILE):
    """Create a task, add it to the list, save, and return the updated list."""
    task = {
        "id": str(uuid4()),
        "course": course,
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "completed": False,
    }
    updated_tasks = tasks + [task]
    save_tasks(updated_tasks, file_path)
    return updated_tasks


def update_task(tasks, task_id, file_path=DATA_FILE, **changes):
    """Update fields of one task by its ID."""
    updated_tasks = []
    for task in tasks:
        if task["id"] == task_id:
            updated_task = {**task, **changes}
            updated_tasks.append(updated_task)
        else:
            updated_tasks.append(task)
    save_tasks(updated_tasks, file_path)
    return updated_tasks


def delete_task(tasks, task_id, file_path=DATA_FILE):
    """Delete one task by its ID."""
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(updated_tasks, file_path)
    return updated_tasks


def get_summary(tasks):
    """Return total, completed, and remaining task counts."""
    completed = sum(1 for task in tasks if task["completed"])
    total = len(tasks)
    return {
        "total": total,
        "completed": completed,
        "remaining": total - completed,
    }
