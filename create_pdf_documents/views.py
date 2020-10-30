from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from view_s.index import index
from view_s.form_s.nowa_wspolnota import nowa_wspolnota
from view_s.form_s.nowy_wlasciciel import nowy_wlasciciel
from view_s.form_s.nowe_naliczenie_wspolnota import nowe_naliczenie_wspolnota
from view_s.form_s.nowe_naliczenie_wlasciciela import nowe_naliczenie_wlasciciela
from view_s.load_wspolnoty import load_wspolnoty
from view_s.wszystkie_wspolnoty import wszystkie_wspolnoty
from view_s.wlasciciele import wlasciciele
from view_s.wszyscy_wlasciciele import wszyscy_wlasciciele
from view_s.wszystkie_naliczenia_wlascicieli import wszystkie_naliczenia_wlascicieli
from view_s.wszystkie_naliczenia_wspolnot import wszystkie_naliczenia_wspolnot
from view_s.naliczenia import naliczenia
from view_s.sorting.sortowanie_naliczen_wlascicieli import sortowanie_naliczen_wlascicieli
from view_s.sorting.sortowanie_naliczen_wspolnot import sortowanie_naliczen_wspolnot
from view_s.sorting.sortowanie_wlascicieli import sortowanie_wlascicieli


"""
View calling login page.
"""
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm


"""
View calling the home page and naliczenia page.
"""
index
naliczenia

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

"""
Views calling templates for all associations, inhabitatnts and documents.
"""
wszystkie_wspolnoty
wlasciciele
wszyscy_wlasciciele
wszystkie_naliczenia_wspolnot
wszystkie_naliczenia_wlascicieli


"""
Basic sorting views
"""
sortowanie_naliczen_wlascicieli
sortowanie_naliczen_wspolnot
sortowanie_wlascicieli