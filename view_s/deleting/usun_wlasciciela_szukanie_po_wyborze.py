from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Mieszkaniec


@login_required
def usun_wlasciciela_szukanie_po_wyborze(request, my_id, wybieracz, szukacz):
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    if request.method == "POST":
        wlasciciel.delete()
        return redirect(f'/wlasciciele/select/{wybieracz}/')
    adres = f'/wlasciciele/select/{wybieracz}/'
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})