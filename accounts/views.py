from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.shortcuts import redirect


def custom_logout(request):
    logout(request)
    return redirect('reminder_app:index')  # Redirect to the desired page