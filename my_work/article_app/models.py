from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class article_model(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title