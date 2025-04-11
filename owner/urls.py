from django.urls import path
from . import views
from django.views.generic.base import TemplateView
app_name = "owner"

urlpatterns = [
    path('register/',views.owner_register, name='register'),
    path('thanks/',
         TemplateView.as_view(
             template_name="owner/registration_complete.html"),
         name="registration-complete"),

]
