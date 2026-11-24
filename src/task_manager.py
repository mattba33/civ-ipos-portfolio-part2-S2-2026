from src.task import Task
from src.file_handler import save_tasks
from src.date_validator import DateValidator
from src.task_display import TaskDisplay

task_display = TaskDisplay()


def load_options():
    """
    Display the available Task Manager menu options.

    Returns:
        None
    """
    task_display.display_options()


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Side Effects:
        - Displays an error message if the title already exists or the due date is
          invalid.
        - Displays a confirmation message when the task is added successfully.
        - Saves the updated task list to a file using `save_tasks`.
    """
    # Prevent duplicate tasks
    if any(task.title == title for task in tasks):
        print("Error: A task with this title already exists.")
        return False

    # Validate due date format
    if not DateValidator.validation_date(due_date):
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return False

    tasks.append(Task(title, description, due_date))
    task_display.display_task_added(title, description, due_date)
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def list_tasks(tasks, status=None):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks by,
            such as "pending" or "completed". Defaults to None.

    Returns:
        None

    Side Effects:
        - Displays the tasks using the TaskDisplay class.
        - Only displays tasks matching the specified status if a
          status filter is provided.
    """
    if status:
        filtered = filter_tasks_by_status(tasks, status)
    else:
        filtered = tasks

    task_display.display_tasks(filtered)


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]
