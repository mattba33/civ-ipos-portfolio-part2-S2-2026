from rich.console import Console
from rich.table import Table


class TaskDisplay():

    def __init__(self, console=None):
        self.console = console or Console()

    def display_tasks(self, tasks):
        table = Table(title="Task Manager")

        table.add_column("Title", style="cyan")
        table.add_column("Description", style="turquoise4")
        table.add_column("Due date", style="red")
        table.add_column("status", style="orange3")

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