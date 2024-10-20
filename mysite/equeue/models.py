
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Geek(models.Model):
    
    name = models.CharField(max_length=200)
    tg_id = models.CharField(max_length=200)
    tg_name = models.CharField(max_length=200)
    status = models.SmallIntegerField()
    create_date = models.DateTimeField(default=timezone.now)    
    start_date = models.DateTimeField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.cancel_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name