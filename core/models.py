from django.db import models

# Create your models here.
class rooms(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name