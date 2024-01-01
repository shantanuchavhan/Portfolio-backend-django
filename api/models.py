# main/models.py

from django.db import models

import cloudinary.models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = cloudinary.models.CloudinaryField('image')
    videos = models.FileField(upload_to='project_videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()