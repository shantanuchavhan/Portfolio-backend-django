# main/models.py

from django.db import models
import cloudinary.models

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = cloudinary.models.CloudinaryField('images', null=True, blank=True)
    categories = models.ManyToManyField(Category)  # Many-to-many relationship with Category
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title



class ContactSubmission(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
