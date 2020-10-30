from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from view_s.index import index
from view_s.form_s.nowa_wspolnota import nowa_wspolnota
from view_s.form_s.nowy_wlasciciel import nowy_wlasciciel
from view_s.form_s.nowe_naliczenie_wspolnota import nowe_naliczenie_wspolnota
from view_s.form_s.nowe_naliczenie_wlasciciela import nowe_naliczenie_wlasciciela
from view_s.load_wspolnoty import load_wspolnoty

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
Views calling new associations, wlasciciel, naliczenia wspolnoty, naliczenia wlasciciela forms.
"""
nowa_wspolnota
nowy_wlasciciel
nowe_naliczenie_wspolnota
nowe_naliczenie_wlasciciela

"""
The function downloads the inhabitants of a given community to the form.
"""
load_wspolnoty