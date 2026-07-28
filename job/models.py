from django.db import models
from django import forms
choisces = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
]
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=choisces, default='Full Time')
    location = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
