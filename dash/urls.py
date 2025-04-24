from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as dash_views
app_name = "dash"

urlpatterns = [
    path('', dash_views.dashboard, name='dashboard'),
    path('login/', dash_views.MyLoginView.as_view(), name='user-login'),
   ]