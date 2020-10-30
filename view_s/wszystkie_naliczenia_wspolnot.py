from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from create_pdf_documents.models import Naliczenie_cala_wspolnota
from create_pdf_documents.forms import Sortowanie_naliczen_wspolnotForm


@login_required
def wszystkie_naliczenia_wspolnot(request):
    form = Sortowanie_naliczen_wspolnotForm(request.POST or None)
    form2= WyborForm(request.POST or None)
    sort = form['parametry_sortowania_wspolnot'].value()
    wybor = form2['wybor_wspolnoty'].value()
    if form.is_valid():
        return redirect(f'/naliczenia/wspolnoty/order/{sort}')
    if form2.is_valid():
        return redirect(f'/naliczenia/wspolnota/select/{wybor}')
    wszystkie = Naliczenie_cala_wspolnota.objects.all().order_by('-data_utworzenia','-data_dokumentu','-data_obowiazywania_oplat','wspolnota__wspolnota')
    return render(request, 'naliczenia_wspolnot.html', {'all': wszystkie, 'form': form, 'form2': form2})