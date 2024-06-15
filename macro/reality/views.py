# app/views.py

from .email_utils import send_email_with_template
from django.http import HttpResponse

def my_email_template_view(request):
    # ... Your view logic ...

    subject = 'Premium Notifications'
    recipient_list = ['francisnjaramba2@gmail.com']
    template_name = 'email.html'
    context = {'username': 'Team member', 'verification_link': 'http://example.com/verify/123/'}

    send_email_with_template(subject, recipient_list, template_name, context)

    # ... Rest of your view logic ...
    return HttpResponse("Email with Template Sent Successfully!")