from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from view_s.index import index
from view_s.form_s.nowa_wspolnota import nowa_wspolnota
from view_s.form_s.nowy_wlasciciel import nowy_wlasciciel
from view_s.form_s.nowe_naliczenie_wspolnota import nowe_naliczenie_wspolnota
from view_s.form_s.nowe_naliczenie_wlasciciela import nowe_naliczenie_wlasciciela

"""
View calling login page.
"""
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


"""
View calling the home page.
"""
index


"""
View calling new associations form_s.
"""
nowa_wspolnota


"""
View calling new wlasciciel form_s.
"""
nowy_wlasciciel


"""
View calling new naliczenie wspólnoty form_s.
"""
nowe_naliczenie_wspolnota


"""
View calling new naliczenie wlasciciela form_s.
"""
nowe_naliczenie_wlasciciela