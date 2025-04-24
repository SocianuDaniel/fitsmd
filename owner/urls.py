from django.urls import path
from . import views  as owner_views
from django.views.generic.base import TemplateView
app_name = "owner"

urlpatterns = [

    path('register/',owner_views.owner_register, name='register'),
    path('thanks/',
         TemplateView.as_view(
             template_name="owner/registration_complete.html"),
         name="registration-complete"),

]
