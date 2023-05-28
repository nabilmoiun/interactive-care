from django.urls import path

from .views import SendEmailToListOfUsers


urlpatterns = [
    path('send-emails/', SendEmailToListOfUsers.as_view(), name='send-emails'),
]