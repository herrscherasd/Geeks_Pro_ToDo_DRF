from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название')
    description = models.TextField(
        verbose_name='Описание'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='Статус таска'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания таска'
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Таск'
        verbose_name_plural = 'Таски'