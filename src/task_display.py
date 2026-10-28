from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from rich import box

class TaskDisplay():

    def __init__(self, console=None):
        self.console = console or Console()

    def display_tasks(self, tasks):
        table = Table(
                    title=f"[cadet_blue][bold]List of Tasks[bold][cadet_blue]", 
                    border_style="cadet_blue", 
                    show_lines=True, 
                    box=box.HEAVY)

        table.add_column(f"[cyan]Title[cyan]", style="cyan", )
        table.add_column(f"[turquoise4]Description[turquoise4]", style="turquoise4")
        table.add_column(f"[red]Due date[red]", style="red")
        table.add_column(f"[orange3]status[orange3]", style="orange3")

        for task in tasks:
            table.add_row(
                task.title,
                task.description,
                task.due_date,
                task.status)

        if not tasks:
            self.console.print("[yellow]No tasks found.[/yellow]")
            return

        self.console.print(table)

    
    def display_options(self):

        panel = Panel(
                    f"[blue]1. Add Task[blue]\n"
                    f"[red]2. Delete Task[red]\n"
                    f"[yellow]3. List Tasks[yellow]\n"
                    f"[dark_green]4. Exit[dark_green]",
                    title="Task Manager CLI",
                    border_style="purple",
                    width=self.console.width // 2)
        
        self.console.print(panel)

    def display_task_added(self, title, description, due_date):
        content += f"[green] Task Created Successfully [green]\n\n"
        content += f"[bold]Title: {title} [bold]\n"
        content += f"[bold]Description {description} [bold]\n"
        content += f"[bold]Due Date: {due_date} [bold]\n"

        panel = Panel(content, title="New Task", border_style="blue")
        self.console.print()