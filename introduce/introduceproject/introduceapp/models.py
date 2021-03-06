from django.db import models

# Create your models here.

class Introduce(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.CharField(max_length = 100)
    date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


    