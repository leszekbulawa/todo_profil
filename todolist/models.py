from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)
    done_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)

    def add_task(self):
        self.created_date = timezone.now()
        self.save()

    def accept_task(self):
        self.done_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
