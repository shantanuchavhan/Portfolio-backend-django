from django.urls import path
from .views import ProjectListView, contact_submission
from .views import get_projects

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<str:category>/', get_projects, name='get_projects_by_category'),
    path('contact/', contact_submission, name='contact-submission'),
]