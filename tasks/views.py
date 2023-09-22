from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import filters

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
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')