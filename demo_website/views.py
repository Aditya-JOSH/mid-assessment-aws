from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests
import pysftp
import urllib.request
import io
from django.contrib import messages
from rest_framework.response import Response

# Create your views here.



from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
import random

from smtplib import SMTPException

from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
import random
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse  
from demo import settings  
from django.core.mail import send_mail  
from django.contrib.sessions.backends.db import SessionStore


@csrf_exempt
def download(request):
    return render(request, 'demo_website/download_file.html')
  
@csrf_exempt
def receive_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            otp = '1000'   # define the otp variable
             
            try:
                send_mail(
                    'OTP',
                    f'{otp}',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                )
                return redirect('verify_otp')
            except:
                # handle email sending error
                return render(request, 'demo_website/receive_otp.html', {'error': 'Error sending OTP'})
    return render(request, 'demo_website/receive_otp.html')

@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        Otp = request.POST.get('otp')
         # Retrieve otp from session
        otp = f"1000"
        if Otp == otp:
            
            return render(request, 'demo_website/download_file.html')
        else:
            # handle invalid OTP input
            return render(request, 'demo_website/verify_otp.html', {'error': 'Invalid OTP'})
    return render(request, 'demo_website/verify_otp.html')

# views.py
from django.shortcuts import render, redirect
from .models import Task

def task_manager(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        end_date = request.POST.get('end_date')
        task = Task(title=title, end_date=end_date)
        task.save()
        return redirect('task_manager')

    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('task_manager')
