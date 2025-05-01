from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField

class OwnerCreationForm(UserCreationForm):
    """Form for creating a owner"""
    captcha = ReCaptchaField()
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1','password2']

