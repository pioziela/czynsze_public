from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec


@login_required
def wszystkie_naliczenia_wlascicieli(request):
    form = Sortowanie_naliczen_wlascicieliForm(request.POST or None)
    form2= WyborForm(request.POST or None)
    sort = form['parametry_sortowania_wlascicieli'].value()
    wybor = form2['wybor_wspolnoty'].value()
    if form.is_valid():
        return redirect(f'/naliczenia/wlascicieli/order/{sort}')
    if form2.is_valid():
        return redirect(f'/naliczenia/wlascicieli/select/{wybor}')
    wszystkie = Naliczenie_jeden_mieszkaniec.objects.all().order_by('-data_utworzenia', 'wspolnota__wspolnota', 'wlasciciel', '-data_dokumentu','-data_obowiazywania_oplat',)
    return render(request, 'naliczenia_mieszkaniec.html', {'all': wszystkie, 'form': form, 'form2': form2})