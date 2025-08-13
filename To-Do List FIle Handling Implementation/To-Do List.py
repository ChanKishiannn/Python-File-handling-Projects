file_name = "To-Do List Files.txt"

open(file_name, "a").close()

def view_tasks():
    with open(file_name, "r") as f:
        tasks = f.readlines()
    if tasks:
        print("\n========== To-Do List ==========")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    else:
        print("\nNo tasks found.")

def add_task():
    task = input("Enter Task you want to add: ")
    with open(file_name, "a") as f:
        f.write(task + "\n")
    print("Task added successfully!")

def edit_task():
    with open(file_name, "r") as f:
        tasks = f.readlines()

    task_to_replace = input("Enter the exact task you want to replace: ")
    new_task = input("Enter the new task: ")

    found = False
    for i in range(len(tasks)):
        if tasks[i].strip() == task_to_replace:
            tasks[i] = new_task + "\n"
            found = True
            break

    if found:
        with open(file_name, "w") as f:
            f.writelines(tasks)
        print("Task updated successfully!")
    else:
        print("No similar task found!")

def delete_task():
    with open(file_name, "r") as f:
        tasks = f.readlines()

    task_to_delete = input("Enter the exact task you want to delete: ")

    new_tasks = [task for task in tasks if task.strip() != task_to_delete]

    if len(new_tasks) != len(tasks):
        with open(file_name, "w") as f:
            f.writelines(new_tasks)
        print("Task deleted successfully!")
    else:
        print("No similar task found!")

# Main Program Loop
userChoose = 0
while userChoose != 5:
    print("\n[1] Add Task")
    print("[2] Edit Task")
    print("[3] Delete Task")
    print("[4] View Tasks")
    print("[5] Exit")

    try:
        userChoose = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if userChoose == 1:
        add_task()
    elif userChoose == 2:
        edit_task()
    elif userChoose == 3:
        delete_task()
    elif userChoose == 4:
        view_tasks()
    elif userChoose == 5:
        print("Goodbye!")
    else:
        print("Invalid choice! Please try again.")
