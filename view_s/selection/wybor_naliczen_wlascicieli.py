from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import WyborForm, Sortowanie_naliczen_wlascicieliForm
from create_pdf_documents.models import Wspolnota, Naliczenie_jeden_mieszkaniec


@login_required
def wybor_naliczen_wlascicieli(request, wybieracz):
    form = Sortowanie_naliczen_wlascicieliForm(request.POST or None)
    form2= WyborForm(request.POST or None)
    sort = form['parametry_sortowania_wlascicieli'].value()
    wybor2 = form2['wybor_wspolnoty'].value()
    wybor = wybieracz
    wybrane = Naliczenie_jeden_mieszkaniec.objects.filter(wspolnota=wybor)
    wspolnota = Wspolnota.objects.get(id=wybieracz)
    if form.is_valid():
        return redirect(f'/naliczenia/wlascicieli/select/{wybor}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/naliczenia/wlascicieli/select/{wybor2}')
    return render(request, 'wybor_naliczen_wlascicieli.html', {'wybrane': wybrane, 'form': form, 'form2': form2, 'wspolnota': wspolnota, 'wybor': wybor})