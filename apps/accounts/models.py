# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField


class User(AbstractUser):
    USER_TYPE = (
        ('Author', 'Author'),
        ('Collaborator', 'Collaborator'),
    )
    uid = ShortUUIDField()
    user_type = models.CharField(max_length=12, choices=USER_TYPE)

    def __str__(self):
        return f'({self.username}) - {self.user_type}'