from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from create_pdf_documents.forms import WyborForm, WyszukajForm, SortowanieForm
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def wybor_wlascicicieli_wspolnoty(request, wybieracz):
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
    wybor2 = form3['wybor_wspolnoty'].value()
    wybor = wybieracz
    wybrane = Mieszkaniec.objects.filter(wspolnota=wybor).order_by('adres_numer_mieszkania').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
    wspolnota = Wspolnota.objects.get(id=wybieracz)
    id = wybieracz
    if form.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/wlasciciele/select/{wybor}/filter/{szukaj}')
    if form3.is_valid():
        return redirect(f'/wlasciciele/select/{wybor2}')
    return render(request, 'wybor_wlascicieli.html', {'wybrane': wybrane, 'form': form, 'form2': form2, 'form3': form3, 'date': date, 'wspolnotaa': wspolnota, 'id': id})