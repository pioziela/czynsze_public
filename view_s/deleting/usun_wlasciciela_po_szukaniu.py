from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Mieszkaniec


@login_required
def usun_wlasciciela_po_szukaniu(request, my_id, szukacz):
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    if request.method == "POST":
        wlasciciel.delete()
        return redirect(f'/wlasciciele/filter/{szukacz}/')
    adres = f'/wlasciciele/filter/{szukacz}/'
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})