from django.db import models
from groups.models import Group


class User(models.Model):
    username = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
