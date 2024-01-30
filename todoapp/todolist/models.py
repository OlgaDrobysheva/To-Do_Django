from django.db import models


# Create your models here.

class ToDo(models.Model):
    title = models.CharField('The Name of Task', max_length=500)
    is_complete = models.BooleanField('Done', default=False)

    class Meta:
        verbose_name = 'The Task'
        verbose_name_plural = 'All Tasks'

    def __str__(self):
        return self.title
