from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=255)
    Singer = models.CharField(max_length=255)
    is_listen = models.BooleanField(default=False)

    def __str__(self):
        return self.title