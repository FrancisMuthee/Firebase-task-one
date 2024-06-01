from django.shortcuts import render

# Create your views here.
def send(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        email = request.POST['email']
        message = request.POST['message']
        transaction_code = request.POST['transaction_code']

        