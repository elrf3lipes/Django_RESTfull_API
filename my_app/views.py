from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from my_app.models import Todo
from rest_framework import serializers

# Create your views here.


class TodoView(APIView):

    def post(self, request):
        task = request.data.get('task', '')
        completed = request.data.get('completed', False)
        todo = Todo.objects.create(task=task, completed=completed)
        return Response(status=201)  # Use status code 201 for resource creation

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodoSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(default=False)


"""
TodoView:

post method: Handles HTTP POST requests to create a new Todo item. 
It extracts 'task' and 'completed' data from the request, creates a new Todo object, 
and returns a response with a 201 status code for successful resource creation.

get method: Handles HTTP GET requests to retrieve all Todo items. 
It queries all Todo objects from the database, serializes them using TodoSerializer, 
and returns the serialized data in the response.

TodoSerializer:

Defines the serialization and deserialization rules for the Todo model.
It has two fields: 'task' (a character field with a maximum length of 200 characters) 
and 'completed' (a boolean field with a default value of False).
"""

