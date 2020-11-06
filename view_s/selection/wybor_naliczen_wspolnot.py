from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from create_pdf_documents.forms import WyborForm, Sortowanie_naliczen_wspolnotForm
from create_pdf_documents.models import Wspolnota, Naliczenie_cala_wspolnota


@login_required
def wybor_naliczen_wspolnot(request, wybieracz):
    form = Sortowanie_naliczen_wspolnotForm(request.POST or None)
    form2= WyborForm(request.POST or None)
    sort = form['parametry_sortowania_wspolnot'].value()
    wybor2 = form2['wybor_wspolnoty'].value()
    wybor = wybieracz
    wybrane = Naliczenie_cala_wspolnota.objects.filter(wspolnota=wybor)
    wspolnota = Wspolnota.objects.get(id=wybieracz)
    if form.is_valid():
        return redirect(f'/naliczenia/wspolnoty/select/{wybor}/order/{sort}')
    if form2.is_valid():
        return redirect(f'/naliczenia/wspolnota/select/{wybor2}')
    return render(request, 'wybor_naliczen_wspolnot.html', {'wybrane': wybrane, 'form': form, 'form2': form2, 'wspolnota': wspolnota, 'wybor': wybor})