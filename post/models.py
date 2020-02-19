from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Data Base tables

class Post(models.Model):
    '''
    new table
    all Post have a default id
    '''
    # self.pk = Primary Key 
    title = models.CharField(max_length=25)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Relation 1 -> N
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Extend features
    class Meta:
        ordering = ['-created'] # '-' delante de la ordenación para que sea del revés
        
    def __str__(self):
        return f'({self.pk}) - {self.title} : {self.content}'