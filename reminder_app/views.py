from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Reminder
from django.contrib.auth import login
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.
# This is what is shown on screen/to the user.


def index(request):
    return render(request, 'reminder_app/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('reminder_app:index')  # If the User is created and valid -> login.
    else:
        form = UserCreationForm()  # Display blank registration form
    return render(request, 'registration/register.html', {'form': form})


@login_required
def reminder_list(request):
    reminder_app = Reminder.objects.filter(user=request.user)
    return render(request, 'reminder_app/reminder_list.html',
                  {'reminder_app': reminder_app})


@login_required
def add_reminder(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        reminder_time = request.POST['reminder_time']
        interval = request.POST['interval']
        Reminder.objects.create(user=request.user, title=title,
                                description=description,
                                reminder_time=reminder_time,
                                interval=interval,
                                )
        return redirect('reminder_app:reminder_list')
    return render(request, 'reminder_app/add_reminder.html')


def send_reminder_email(reminder):
    send_mail(
        f"Reminder: {reminder.title}",
        reminder.description,
        'williamgeesey@gmail.com',
        [reminder.user.email],
        fail_silently=False
    )
