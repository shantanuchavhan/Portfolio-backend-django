# main/views.py

from rest_framework import generics
from .models import Project,Category
from .serializers import ProjectSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import activate


class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language', 'en')  # Default to English if language is not specified
        activate(language)  # Activate the specified language for translations
        return Project.objects.filter(language__code=language)


def get_projects(request, category=None):
    projects = Project.objects.all()

    if category:
        category_instance = get_object_or_404(Category, name=category)
        projects = projects.filter(categories=category_instance)

    project_data = [
        {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'images': str(project.images),
        }
        for project in projects
    ]

    return JsonResponse(project_data, safe=False)



@csrf_exempt
@require_POST
def contact_submission(request):
    try:
        data = json.loads(request.body)
        print(data,"data")
        form = ContactForm(data)
        send_mail(
                'New Contact Form Submission',
                f'Email: {data["email"]}\nSubject: {data["subject"]}\nMessage: {data["message"]}',
                'shantanuchavhan002@gmail.com',
                [f'{data["email"]}'],
                fail_silently=False,
            )


        if form.is_valid():
            form.save()

            
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data'})

