from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class rooms(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name