from django.core.management.base import BaseCommand, CommandError
from backend.api.models import Todo


class Command(BaseCommand):
    help = "Populates the DB with some initial data"

    def handle(self, *args, **kwargs):
        todos = [
            {
                "id": "1",
                "task": "First task",
                "complete": True,
            },
            {
                "id": "2",
                "task": "Second task",
                "complete": False,
            },
        ]
        for todo in todos:
            newTodo = Todo(task=todo["task"], complete=todo["complete"])
            newTodo.id = todo["id"]
            newTodo.save()
