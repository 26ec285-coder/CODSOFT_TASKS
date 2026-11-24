
import json
import os

FILE_NAME = "tasks.json"


# Load saved tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved tasks. Starting with an empty list.")

    return []


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):
    task = input("Enter your task: ").strip()

    if task:
        tasks.append({
            "task": task,
            "completed": False
        })

        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# View all tasks
def view_tasks(tasks):
    print("\n========== YOUR TASKS ==========")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"{index}. {task['task']} - {status}")


# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main application
def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
