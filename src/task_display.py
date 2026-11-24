
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box


class TaskDisplay:
    """
    A class to handle the terminal display of tasks and menu options
    using the Rich library.
    """

    def __init__(self, console=None):
        """
        Initialise the TaskDisplay with a Rich Console instance.

        Args:
            console (Console, optional): A Rich Console instance.
            Defaults to a new Console.
        """
        self.console = console or Console()

    def display_tasks(self, tasks):
        """
        Display tasks in a formatted Rich table.

        Args:
            tasks (list): A list of Task objects containing task details.

        Returns:
            None
        """
        table = Table(
            title="[cadet_blue][bold]List of Tasks[/bold][/cadet_blue]",
            border_style="cadet_blue",
            show_lines=True,
            box=box.HEAVY
        )

        table.add_column("[cyan]Title[/cyan]", style="cyan")
        table.add_column(
            "[turquoise4]Description[/turquoise4]",
            style="turquoise4"
        )
        table.add_column("[red]Due date[/red]", style="red")
        table.add_column("[orange3]Status[/orange3]", style="orange3")

        for task in tasks:
            table.add_row(
                task.title,
                task.description,
                task.due_date,
                task.status
            )

        if not tasks:
            self.console.print("[yellow]No tasks found.[/yellow]")
            return

        self.console.print(table)

    def display_options(self):
        """
        Display the main menu options inside a Rich panel.

        Returns:
            None
        """
        panel = Panel(
            "[blue]1. Add Task[/blue]\n"
            "[red]2. Delete Task[/red]\n"
            "[yellow]3. List Tasks[/yellow]\n"
            "[dark_green]4. Exit[/dark_green]",
            title="Task Manager CLI",
            border_style="purple",
            width=self.console.width // 2
        )

        self.console.print(panel)

    def display_task_added(self, title, description, due_date):
        """
        Display a success message and the details of a newly created task.

        Args:
            title (str): The title of the created task.
            description (str): A brief description of the created task.
            due_date (str): The due date of the created task.

        Returns:
            None
        """
        content = (
            "[green]Task Created Successfully[/green]\n\n"
            f"[bold]Title:[/bold] {title}\n"
            f"[bold]Description:[/bold] {description}\n"
            f"[bold]Due Date:[/bold] {due_date}"
        )

        panel = Panel(
            content,
            title="New Task",
            border_style="blue",
            width=self.console.width // 2
        )

        self.console.print(panel)
