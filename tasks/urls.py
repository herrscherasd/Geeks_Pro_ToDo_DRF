from rest_framework.routers import DefaultRouter

from tasks.views import TaskAPIViewSet

router = DefaultRouter()

router.register('tasks', TaskAPIViewSet, basename='tasks')

urlpatterns = router.urls