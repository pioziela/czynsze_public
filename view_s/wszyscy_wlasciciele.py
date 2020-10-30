from datetime import datetime
from django.contrib.auth.decorators import login_required
from create_pdf_documents.models import Mieszkaniec, Wspolnota
from django.shortcuts import render, redirect


@login_required
def wszyscy_wlasciciele(request, my_id):
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
    sort = form['parametry_sortowania'].value()
    szukaj = form2['wyszukaj'].value()
    adres = f'/nowy_wlasciciel/{my_id}/wszyscy/'
    if form.is_valid():
        return redirect(f'/wlasciciele/select/{my_id}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/wlasciciele/select/{my_id}/filter/{szukaj}')
    wszyscy = Mieszkaniec.objects.all().filter(wspolnota=my_id).order_by('adres_numer_mieszkania', 'nazwisko', 'imie').filter(dane_od__lte=f'{year_od}-{month_od}-{day}', dane_do__gte=f'{year_do}-{month_do}-{day}')
    wspolnota = Wspolnota.objects.get(id=my_id)
    wszyscy_historia = Mieszkaniec.objects.all().filter(wspolnota=my_id).order_by('adres_numer_mieszkania', 'nazwisko', 'imie')
    return render(request, 'wszyscy_wlasciciele.html', {'all': wszyscy, 'form': form, 'form2': form2, 'date': date, 'wspolnota': wspolnota, 'wszyscy_historia': wszyscy_historia, 'my_id': my_id, 'adres': adres})