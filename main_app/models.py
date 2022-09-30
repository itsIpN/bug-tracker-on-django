from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

defaultUser = User

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 2500)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('project_details', kwargs={'project_id' : self.id})

class Bugs(models.Model):
    status_choice =(("Not being worked on", "Not being worked on"), ("Work in Progress", "Work in Progress"), ("Fixed", "Fixed"))
    priority_choice=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    title = models.CharField(max_length = 100)
    comments = models.TextField(max_length = 2500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length = 50, choices=status_choice)
    assigned_to = models.ManyToManyField(User)
    priority = models.IntegerField(choices=priority_choice)
    fixed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bug_details', kwargs={'bug_id' : self.id})
