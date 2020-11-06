from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime
from create_pdf_documents.forms import WyborForm, WyszukajForm, SortowanieForm
from create_pdf_documents.models import Mieszkaniec


@login_required
def wyszukiwanie(request, szukacz):
    date = datetime.today().strftime("%Y-%m-%d")
    date2 = datetime.today()
    day, month, year = date2.day, date2.month, date2.year
    if day == 31:
        day = 30
    if month > 1 and month <= 11:
        if month == 3 and day > 28:
            day = 28
        month_od = month + 1
        year_od = year
        month_do = month - 1
        year_do = year
    elif month == 1:
        if day > 28:
            day = 28
        month_od = month + 1
        year_od = year
        month_do = 12
        year_do = year - 1
    elif month == 12:
        month_od = 1
        year_od = year + 1
        month_do = month - 1
        year_do = year
    form = SortowanieForm(request.POST or None)
    form2 = WyszukajForm(request.POST or None)
    form3 = WyborForm(request.POST or None)
    sort = form['parametry_sortowania'].value()
    szukaj = form2['wyszukaj'].value()
    wybor = form3['wybor_wspolnoty'].value()
    lenght = 0
    adres = f'/nowy_wlasciciel/'
    if form.is_valid():
        return redirect(f'/wlasciciele/order/{sort}')
    if form2.is_valid():
        return redirect(f'/wlasciciele/filter/{szukaj}')
    if form3.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}')
    szukaj = szukacz
    regularne = f"(.*){szukaj}(.*)"
    wyszukanie = Mieszkaniec.objects.filter(Q(nazwisko__iregex=fr'{regularne}') | Q(imie__iregex=fr'{regularne}')).filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
    return render(request, 'szukanie.html', {'szukaj': wyszukanie, 'form': form, 'form2': form2, 'form3': form3, 'date': date, 'szukacze': szukaj, 'lenght': lenght, 'adres': adres})