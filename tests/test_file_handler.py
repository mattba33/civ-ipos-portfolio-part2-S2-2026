import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_handler import load_tasks, save_tasks  # noqa: E402
from src.task import Task  # noqa: E402


TEST_FILE = "test_tasks.bin"


class TestFileHandler(unittest.TestCase):
    """
    Unit tests for file handling functionalities including saving tasks
    to a binary file and loading them back.
    """

    def setUp(self):
        """
        Set up the test environment by creating sample tasks
        and backing up the original task binary file.
        """
        self.original_file = "tasks.bin"

        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        os.rename("tasks.bin", TEST_FILE) if os.path.exists("tasks.bin") else None

        self.sample_tasks = [
            Task("Task 1", "Description 1", "12-12-2024", "pending"),
            Task("Task 2", "Description 2", "15-12-2024", "completed"),
        ]

    def tearDown(self):
        """
        Clean up the test environment by removing test-created binary files
        and restoring the original task binary file.
        """
        if os.path.exists("tasks.bin"):
            os.remove("tasks.bin")

        os.rename(TEST_FILE, "tasks.bin") if os.path.exists(TEST_FILE) else None

    def test_file_content(self):
        """
        Test saving tasks to a binary file and loading them back.
        Verify that the saved tasks are loaded with the correct details.
        """
        save_tasks(self.sample_tasks)

        tasks = load_tasks()

        self.assertEqual(len(tasks), 2)

        self.assertEqual(tasks[0].to_dict(), self.sample_tasks[0].to_dict())
        self.assertEqual(tasks[1].to_dict(), self.sample_tasks[1].to_dict())


if __name__ == "__main__":
    unittest.main()
