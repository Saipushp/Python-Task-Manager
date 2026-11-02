from tasks import add_task, view_tasks
from tasks import complete_task, delete_task

print("Welcome to Python Task Manager!")

while True:

    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    # Remove extra spaces from user input
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task_name = input("Enter task name: ").strip()

        if task_name:
            add_task(task_name)
        else:
            print("Task name cannot be empty!")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        try:
            task_number = int(input("Enter task number to complete: ").strip())
            complete_task(task_number)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        view_tasks()
        try:
            task_number = int(input("Enter task number to delete: ").strip())
            delete_task(task_number)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        print("Thank you for using Task Manager!")
        break

    else:
        print("Invalid choice! Please try again.")