tasks = []

# Function to add a task to the to-do list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added: " + task)

# Function to remove a task from the to-do list
def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        try:
            task_number = int(input("Enter the number of the task to remove:"))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Task removed: " + removed_task)
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to display the to-do list
def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Main program loop
while True:
    print("\nTo-Do List Program")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")