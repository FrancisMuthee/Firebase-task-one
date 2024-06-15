# app/views.py

from .email_utils import send_email_with_template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.models import auth

def index(request):
    return render(request, 'index.html')

def my_email_template_view(request):
    # ... Your view logic ...

    subject = 'Premium Notifications'
    recipient_list = ['francisnjaramba2@gmail.com']
    template_name = 'email.html'
    context = {'username': 'Team member', 'verification_link': 'http://example.com/verify/123/'}

    send_email_with_template(subject, recipient_list, template_name, context)

    # ... Rest of your view logic ...
    return HttpResponse("Email with Template Sent Successfully!")

def base(request):
    return render(request, 'base.html')


# app/views.py
# app/views.py



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Add validation here if needed
        if not name or not email or not password:
            messages.error(request, 'Please fill out all fields.')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        # Create the user instance
        user = User(name=name, email=email)
        
        # Save the user to the database
        user.save()
        print('User created')
        return redirect('success')  # Redirect to a success page

    return render(request, 'reg.html')

def success(request):
    return render(request, 'success.html')



