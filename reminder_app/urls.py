from django.urls import path, include

from . import views

app_name = 'reminder_app'
urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name='register'),
    path('add/', views.add_reminder, name='add_reminder'),
    path('reminder_list/', views.reminder_list, name='reminder_list'),
]