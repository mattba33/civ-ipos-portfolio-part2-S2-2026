import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rich.console import Console  # noqa: E402
from src.task_display import TaskDisplay  # noqa: E402
from src.task import Task  # noqa: E402


class TestTaskDisplay(unittest.TestCase):
    """
    Unit tests for TaskDisplay functionalities including displaying tasks,
    menu options, empty task lists, and task creation messages.
    """

    def setUp(self):
        """
        Set up the test environment by creating a recorded Rich Console
        and initialising a TaskDisplay instance.
        """
        self.console = Console(record=True, width=100)
        self.task_display = TaskDisplay(self.console)

    def test_display_tasks(self):
        """
        Test displaying tasks in a formatted Rich table.
        Verify that the table title and task details appear in the output.
        """
        tasks = [
            Task("Test Task", "Test Description", "12-12-2024", "pending")
        ]

        self.task_display.display_tasks(tasks)

        output = self.console.export_text()

        self.assertIn("List of Tasks", output)
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
        self.assertIn("12-12-2024", output)
        self.assertIn("pending", output)

    def test_display_empty_tasks(self):
        """
        Test displaying an empty task list.
        Verify that the appropriate message is displayed when no tasks exist.
        """
        self.task_display.display_tasks([])

        output = self.console.export_text()

        self.assertIn("No tasks found.", output)

    def test_display_options(self):
        """
        Test displaying the main menu options.
        Verify that all four menu options appear in the output.
        """
        self.task_display.display_options()

        output = self.console.export_text()

        self.assertIn("Add Task", output)
        self.assertIn("Delete Task", output)
        self.assertIn("List Tasks", output)
        self.assertIn("Exit", output)

    def test_display_task_added(self):
        """
        Test displaying the task creation success message.
        Verify that the success message and task details appear in the output.
        """
        self.task_display.display_task_added(
            "Test Task",
            "Test Description",
            "12-12-2024"
        )

        output = self.console.export_text()

        self.assertIn("Task Created Successfully", output)
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
        self.assertIn("12-12-2024", output)


if __name__ == "__main__":
    unittest.main()
