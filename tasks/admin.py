from django.contrib import admin

from tasks.models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created']
    list_per_page = 20
    