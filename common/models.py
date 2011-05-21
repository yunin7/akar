from django.db import models


class PostBase(models.Model):
    title = models.CharField(max_length=150)
    short_text =  models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        abstract = True
        ordering = ('-timestamp',)