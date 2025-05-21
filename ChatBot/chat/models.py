from django.db import models
from django.utils import timezone


# Create your models here.
class Prompts(models.Model):
    def __str__(self):
        return self.prompt

    prompt = models.CharField(max_length=500)
    prompt_date = models.DateTimeField("date_prompted", default=timezone.now())
