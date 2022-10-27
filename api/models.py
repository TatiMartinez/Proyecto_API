
from django.db import models

# Create your models here.

class Incoming(models.Model):
    timeStamp = models.DateTimeField(auto_now_add=True)
    conversationId = models.CharField(max_length=500)
    payload = models.CharField(max_length=500)
    botResponse = models.CharField(max_length=500)

