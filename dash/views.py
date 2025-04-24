from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import core
from django.contrib.auth.views import LoginView
# Create your views here.


@login_required
def dashboard(request):

    owner = get_object_or_404(core.models.Owner, user=request.user)
    return render(request, 'dash/dash.html', {'owner': owner})

class MyLoginView(LoginView):
    """Custom login view"""
    template_name = 'dash/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        return super().dispatch(request, *args, **kwargs)
