from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Naliczenie_cala_wspolnota


@login_required
def usun_naliczenie_wspolnoty_po_wyborze_i_po_sortowaniu(request, my_id, wybieracz, sorter):
    naliczenie = get_object_or_404(Naliczenie_cala_wspolnota, pk=my_id)
    adres = f'/naliczenia/wspolnota/select/{wybieracz}/'
    if request.method == "POST":
        naliczenie.delete()
        return redirect(f'/naliczenia/wspolnota/select/{wybieracz}/')
    return render(request, 'usun_naliczenie_wspolnoty.html', {'naliczenie': naliczenie, 'adres': adres})