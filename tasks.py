import json

# File where tasks will be stored
FILE_NAME = "tasks.json"


# Function to load tasks
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Function to save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Function to add a task
def add_task(task_name):
    tasks = load_tasks()

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


# Function to view tasks
def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found!")
        return

    print("\nYour Tasks:")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{index}. {task['task']} - {status}")

        # Function to complete a task
def complete_task(task_number):
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return

    tasks[task_number - 1]["completed"] = True

    save_tasks(tasks)

    print("Task completed successfully!")

    # Function to delete a task
def delete_task(task_number):
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number!")
        return

    removed_task = tasks.pop(task_number - 1)

    save_tasks(tasks)

    print(f"Deleted task: {removed_task['task']}")

