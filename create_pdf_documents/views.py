from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


@login_required
def index(request):
    return render(request, 'index.html')