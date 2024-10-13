from django.urls import path, include
from django.contrib.auth.views import LogoutView

from reminder_app import views
from . import views as accountviews

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("register/", views.register, name='register'),
    path("logout/", LogoutView.as_view(next_page='reminder_app:index'), name='logout'),
]