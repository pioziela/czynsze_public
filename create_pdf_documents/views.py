from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from views.index import index


"""
View calling login page.
"""
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


"""
View calling the home page.
"""
index


