# main/models.py

from django.db import models

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='project_images/', null=True, blank=True)
    videos = models.FileField(upload_to='project_videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
