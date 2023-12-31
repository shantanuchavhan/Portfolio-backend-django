# main/views.py

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm
import json
from django.http import JsonResponse

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer





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

