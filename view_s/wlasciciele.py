from datetime import datetime
from django.contrib.auth.decorators import login_required
from create_pdf_documents.models import Mieszkaniec
from django.shortcuts import render, redirect
from create_pdf_documents.forms import SortowanieForm


@login_required
def wlasciciele(request):
    date = datetime.today().strftime("%Y-%m-%d")
    date2 = datetime.today()
    day, month, year = date2.day, date2.month, date2.year
    if month > 1 and month < 11:
        month_od = month + 1
        year_od = year
        month_do = month - 1
        year_do = year
    elif month == 1:
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
    lenght = 'c'
    if form.is_valid():
        return redirect(f'/wlasciciele/order/{sort}')
    if form2.is_valid():
        return redirect(f'/wlasciciele/filter/{szukaj}')
    if form3.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}')
    wszyscy = Mieszkaniec.objects.all().order_by('wspolnota__wspolnota', 'adres_numer_domu', 'adres_numer_mieszkania', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
    return render(request, 'wlasciciele.html', {'all': wszyscy, 'form': form, 'form2': form2, 'form3': form3, 'date': date, 'lenght': lenght})