import graphene
from graphene_django import DjangoObjectType

from backend.api.models import Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ("task", "complete", "date_added", "id")


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    get_todo = graphene.Field(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_get_todo(root, info, id):
        try:
            todo = Todo.objects.get(pk=id)
            return todo
        except Exception as e:
            print(e)
            return None


# mutations
class CreateTodo(graphene.Mutation):
    class Arguments:
        task = graphene.String()

    ok = graphene.Boolean()
    todo = graphene.Field(lambda: TodoType)

    def mutate(root, info, task):
        todo = Todo(task=task)
        todo.save()
        ok = True
        return CreateTodo(ok=ok, todo=todo)


class EditTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        task = graphene.String()

    ok = graphene.Boolean()
    todo = graphene.Field(lambda: TodoType)

    def mutate(root, info, id, task):
        todo = Todo.objects.get(id=id)
        todo.task = task
        todo.save()

        return EditTodo(ok=True, todo=todo)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    edit_todo = EditTodo.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
