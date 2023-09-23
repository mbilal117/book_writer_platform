from django.contrib.auth.models import User
from django.db import models

from apps.common.models import TimeStampAwareModel
from book_writer_platform import settings


# Create your models here.


class Books(TimeStampAwareModel):
    name = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "books"


class Sections(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, db_column='parent', related_name="children")
    book = models.ForeignKey(Books, related_name='sections', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "sections"

