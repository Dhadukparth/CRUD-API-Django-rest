from django.db import models

# Create your models here.

class todos(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title