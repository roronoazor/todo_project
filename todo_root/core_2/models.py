from django.db import models


# Create your models here.
class Todo(models.Model):

    name = models.CharField(max_length=1000)
    meta = models.TextField(null=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.meta)

