
from src.task_manager import load_options, add_task, delete_task, list_tasks
from src.file_handler import load_tasks


def main():
    """
    Main function for running the Task Manager CLI.

    Loads existing tasks and displays the menu, allowing users to
    add, delete, list tasks, or exit the application.
    """

    tasks = load_tasks()

    while True:

        load_options()

        choice = input("Enter your Choice: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            print("\n\n\n")
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            title = input("Title of the task to delete: ")

            if delete_task(tasks, title):
                print("Task deleted successfully. \n\n\n")
            else:
                print("Task not found.\n\n\n")

        elif choice == "3":
            print("\n\n\n")
            list_tasks(tasks)

        elif choice == "4":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid choice. Try again.\n\n\n")


if __name__ == "__main__":
    main()
