from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import WyborForm, WyszukajForm, SortowanieForm
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def sortowanie_wlascicieli_po_wyborze(request, wybieracz, sorter):
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
    wybor2 = form3['wybor_wspolnoty'].value()
    wybor = wybieracz
    lenght = 'a'
    id = wybieracz
    id2 = sorter
    adres = f'/nowy_wlasciciel/{id}/select/{id2}/'
    if form.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}/filter/{szukaj}')
    if form3.is_valid():
        return redirect(f'/wlasciciele/select/{wybor2}')
    element_sortujacy = sorter
    if element_sortujacy == 'imie':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('imie', 'nazwisko', 'wspolnota__wspolnota').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'imię'
    elif element_sortujacy == 'nazwisko':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('nazwisko', 'wspolnota__wspolnota', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'nazwisko'
    elif element_sortujacy == 'wspolnota':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'wspólnota'
    elif element_sortujacy == 'numer_mieszkania':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('adres_numer_mieszkania','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'numer mieszkania'
    elif element_sortujacy == 'miasto':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('miasto','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'miasto'
    elif element_sortujacy == 'powierzchnia_mieszkania':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-powierzchnia_mieszkania','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'powierzchnia mieszkania'
    elif element_sortujacy == 'zaliczka_CO':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-zaliczka_CO','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'zaliczka C.O.'
    elif element_sortujacy == 'ciepla_woda':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-podgrzanie_wody_objetosc','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'ciepła woda'
    elif element_sortujacy == 'zimna_woda':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-zimna_woda_objetosc','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'zimna woda'
    elif element_sortujacy == 'scieki':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-odprowadzenie_sciekow_objetosc','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'ścieki'
    elif element_sortujacy == 'osoby':
        sortowanie = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('-ilosc_osob','wspolnota__wspolnota', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
        sortowacz = 'osoby'
    wspolnota = Wspolnota.objects.get(id=wybieracz)
    return render(request, 'sortowanie_wlascicieli_po_wyborze.html', {'sortowanie': sortowanie, 'form': form, 'form2': form2, 'form3': form3, 'date': date, 'wybor': wybor, 'sortowacz': sortowacz, 'lenght': lenght, 'wspolnota': wspolnota, 'id': id, 'id2': id2, 'adres': adres})