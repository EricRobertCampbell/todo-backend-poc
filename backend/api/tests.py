from django.test import TestCase
from backend.api.models import Todo
from graphene_django.utils.testing import GraphQLTestCase
from graphene.test import Client
from backend.schema import schema

import json


def generate_fixtures():
    fixtures = [
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
    for fixture in fixtures:
        newTodo = Todo(task=fixture["task"], complete=fixture["complete"])
        newTodo.id = fixture["id"]
        newTodo.save()


# Create your tests here.
class TestAllTodos(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    @classmethod
    def setUpClass(cls):
        super(TestAllTodos, cls).setUpClass()

        cls.query_string = """query { allTodos { task complete } }"""

    def setUp(self):
        generate_fixtures()

    def test_should_return_all_todos(self):
        client = Client(schema)
        executed = client.execute(self.query_string)
        self.assertIn("data", executed, f"")
        self.assertIn("allTodos", executed["data"], f"")
        self.assertEqual(len(executed["data"]["allTodos"]), 2, f"")
        allTodos = executed["data"]["allTodos"]
        self.assertEqual(allTodos[0], {"task": "First task", "complete": True}, f"")
        self.assertEqual(allTodos[1], {"task": "Second task", "complete": False}, f"")
