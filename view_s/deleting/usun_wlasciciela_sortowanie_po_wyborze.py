from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Mieszkaniec


@login_required
def usun_wlasciciela_sortowanie_po_wyborze(request, my_id, wybieracz, where, sorter):
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    adres = ''
    if request.method == "POST":
        wlasciciel.delete()
        if where == 'select':
            return redirect(f'/wlasciciele/select/{wybieracz}/')
        elif where == 'wszyscy':
            return redirect(f'/wspolnota/{wybieracz}/')
    if where == 'select':
        adres = f'/wlasciciele/select/{wybieracz}/'
    elif where == 'wszyscy':
        adres = f'/wspolnota/{wybieracz}/'
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})