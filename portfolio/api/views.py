# main/views.py

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



@csrf_exempt 
@require_POST
def contact_submission(request):
    data = request.POST
    form = ContactForm(data)

    if form.is_valid():
        form.save()

      
        send_mail(
            'New Contact Form Submission',
            f'Email: {form.cleaned_data["email"]}\nSubject: {form.cleaned_data["subject"]}\nMessage: {form.cleaned_data["message"]}',
            'shantanuchavhan002@gmail.com',  
            [f'{form.cleaned_data["email"]}'],  
            fail_silently=False,
        )

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})
