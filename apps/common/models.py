from django.db import models


class TimeStampAwareModel(models.Model):
    """
    A model class that can be used as super class
    for any model that is considered timestamp aware
    model.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)

    def is_deleted(self):
        return True if self.date_deleted else False

    is_deleted.boolean = True

    class Meta:
        abstract = True