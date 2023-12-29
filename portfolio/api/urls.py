from django.urls import path
from .views import ProjectListView, contact_submission

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('contact/', contact_submission, name='contact-submission'),
]