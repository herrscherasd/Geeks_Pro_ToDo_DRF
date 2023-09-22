from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from tasks.models import Task
from tasks.serializer import TaskSerializer

# Create your views here.
class TaskAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer