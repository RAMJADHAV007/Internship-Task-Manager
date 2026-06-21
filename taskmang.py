# Task Management Application
# A simple command-line interface (CLI) to manage daily tasks.

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Completed")
    print("4. Exit")

def view_tasks(tasks):
    """Displays the current list of tasks and their status."""
    if not tasks:
        print("\nNo tasks available. You're all caught up!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['name']}")

def add_task(tasks):
    """Prompts the user to add a new task to the list."""
    task_name = input("Enter the task description: ")
    tasks.append({"name": task_name, "completed": False})
    print(f"\nTask '{task_name}' added successfully!")

def complete_task(tasks):
    """Marks a specific task as completed based on user input."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print("\nTask marked as completed!")
            else:
                print("\nInvalid task number.")
        except ValueError:
            print("\nPlease enter a valid number.")

def main():
    """Main function to run the Task Manager application."""
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("\nExiting Task Manager. Have a productive day!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()