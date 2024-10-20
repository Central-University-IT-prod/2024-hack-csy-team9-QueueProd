from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Geek(models.Model):
    name = models.CharField(max_length = 180)
    tg_name = models.CharField(max_length = 180, null=True)
    tg_id = models.CharField(max_length = 180, null=True)
    create_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)    
    status = models.SmallIntegerField(default=2)
    start_date = models.DateTimeField(blank=True, null=True)
    cancel_date = models.DateTimeField(blank=True, null=True)
    #completed = models.BooleanField(default = False, blank = True)
    #updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name