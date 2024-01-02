from django.contrib import admin
from .models import Project, ContactSubmission,Category

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(ContactSubmission)