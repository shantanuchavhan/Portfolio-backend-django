from django.contrib import admin
from .models import Project, ContactSubmission,Category,Language

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(ContactSubmission)
admin.site.register(Language)