from django.shortcuts import render

import core.models
from core import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from core import models
from django.contrib.auth.decorators import login_required

# Create your views here.


def owner_register(request):
    """Function to register a new owner"""
    if request.method == "POST":
        form = forms.OwnerCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            
            user = get_user_model().objects.create_user(
                email=email, password=password1, level=1
                )
            if user:
                owner = models.Owner()
                owner.user = user

                owner.save()
                return redirect('owner:registration-complete')

        return render(request,'owner/register.html', {'form': form})
    else:
        form = forms.OwnerCreationForm()
        return render(request,'owner/register.html', {'form': form})


    return render(request,'owner/register.html')



