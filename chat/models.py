from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.CharField(max_length=100)
    msg = models.CharField(max_length=100)
    sent_at = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=100)
    sent_to = models.CharField(max_length=100, default='emerie')

    def __str__(self):
        return self.msg
