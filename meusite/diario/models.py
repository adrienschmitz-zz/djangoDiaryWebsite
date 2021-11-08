from django.conf import settings
from django.db import models
from django.utils import timezone


class Day(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    leave_text = models.TextField()
    gratitude_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()
