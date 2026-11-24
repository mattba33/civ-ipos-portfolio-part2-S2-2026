# Task Manager CLI

A Python-based command-line Task Manager application that allows users to create, manage and display tasks. The application uses reusable Python libraries to improve its functionality, date validation and terminal presentation.

## Features

- **Add Tasks:** Create tasks with a title, description and due date.
- **Delete Tasks:** Remove existing tasks using their title.
- **List Tasks:** View existing tasks in a structured table.
- **Duplicate Prevention:** Prevents tasks with duplicate titles from being added.
- **Date Validation:** Uses `python-dateutil` to validate due dates and reject invalid dates.
- **Rich Terminal Interface:** Uses the Rich library to display formatted tables, panels and styled terminal output.
- **File Storage:** Saves and loads tasks using the existing file handling functionality.

## Technologies and Dependencies

The project uses the following Python libraries:

| Library | Purpose |
|---|---|
| Rich | Formats terminal output using tables, panels and colours. |
| python-dateutil | Provides date parsing and validation functionality. |
| unittest | Tests application functionality using Python's built-in testing framework. |
| Flake8 | Checks code quality and compliance with Python style guidelines. |

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd pin_civ_assessment_ipos_portfolio_2
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

For macOS/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the project and dependencies

Install the project in editable mode:

```bash
python -m pip install -e .
```

Install development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Running the Application

To start the Task Manager CLI:

```bash
python main.py
```

The application provides options to:

1. Add a task.
2. Delete a task.
3. List existing tasks.
4. Exit the application.

When creating a task, enter a title, description and due date.

### Due Date Validation

The application uses `python-dateutil` to validate due dates.

Dates must follow the `DD-MM-YY` format.

Examples:

| Input | Result |
|---|---|
| `18-11-26` | Valid date |
| `31-02-26` | Invalid date |
| `32-11-26` | Invalid date |
| `18/11/26` | Incorrect format |

Invalid dates are rejected, and the task will not be added.

## Testing

The project uses Python's built-in `unittest` framework.

To run all unit tests:

```bash
python -m unittest discover -s tests
```

Individual test files can also be executed:

```bash
python3 tests/test_date_validator.py
```

The tests cover:

- Task creation and deletion.
- Duplicate task prevention.
- Date validation.
- Invalid date formats.
- Invalid days and months.
- Rich terminal display functionality.
- File saving and loading.

## Code Quality

The project uses Flake8 to check Python code for style and formatting issues.

Run Flake8 from the project root directory:

```bash
python -m flake8 src/ tests/
```

Resolve any reported issues before submitting changes.

## Project Structure

```text
TaskManager/
│
├── src/
│   ├── main.py
│   ├── task.py
│   ├── task_manager.py
│   ├── file_handler.py
│   ├── task_display.py
│   └── date_validator.py
│
├── tests/
│   ├── test_task_manager.py
│   ├── test_file_handler.py
│   ├── test_task_display.py
│   └── test_date_validator.py
│
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── README.md
└── main.py
```

*Note: The project structure may change as additional functionality is introduced.*

## Development

This project was enhanced as part of the ICTPRG439 assessment, focusing on investigating and integrating reusable components into an existing application.

The improvements include:

- Integration of the Rich library to improve terminal presentation.
- Integration of python-dateutil to improve due date validation.
- Additional unit tests to verify new and existing functionality.
- Updated documentation to reflect the application's improvements.

GitHub Issues and Pull Requests are used to track changes, document improvements and review code before merging into the main branch.