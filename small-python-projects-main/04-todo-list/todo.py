
# Project 04 - To-Do List that saves to file
<<<<<<< HEAD
#wassim made a change
=======

>>>>>>> origin/feature-ali
FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


tasks = load_tasks()

print("--- Your To-Do List ---")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("5. Count Tasks")
    print("6. Delete All Tasks")

    choice = input("Choose (1-6): ")

    if choice == '1':
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '2':
        new_task = input("Enter new task: ")

        if new_task.strip():
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Added: '{new_task}'")
        else:
            print("Task cannot be empty!")

    elif choice == '3':
        if not tasks:
            print("Nothing to delete!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to delete: "))

                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    elif choice == '4':
        print("Bye! Your tasks are saved in tasks.txt")
        break

    elif choice == '5':
        print(f"\nTotal number of tasks: {len(tasks)}")

    elif choice == '6':
        if not tasks:
            print("No tasks to delete!")
        else:
            confirmation = input("Are you sure? (yes/no): ")

            if confirmation.lower() == "yes":
                tasks.clear()
                save_tasks(tasks)
                print("All tasks deleted!")
            else:
                print("Deletion cancelled!")

    else:
        print("Invalid choice! Please choose between 1 and 6.")
