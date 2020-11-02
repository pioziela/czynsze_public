from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec


@login_required
def usun_naliczenie_wlasciciela_po_wyborze_i_po_sortowaniu(request, my_id, wybieracz, sorter):
    naliczenie = get_object_or_404(Naliczenie_jeden_mieszkaniec, pk=my_id)
    adres = f'/naliczenia/wlascicieli/select/{wybieracz}/'
    if request.method == "POST":
        naliczenie.delete()
        return redirect(f'/naliczenia/wlascicieli/select/{wybieracz}/')
    return render(request, 'usun_naliczenie_wlasciciela.html', {'naliczenie': naliczenie, 'adres': adres})