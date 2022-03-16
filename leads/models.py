from django.db import models
class Lead(models.Model): 
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)