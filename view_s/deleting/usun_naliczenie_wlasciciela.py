from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec
from view_s.wszystkie_naliczenia_wlascicieli import wszystkie_naliczenia_wlascicieli


@login_required
def usun_naliczenie_wlasciciela(request, my_id):
    adres = f'/naliczenia_mieszkaniec/'
    naliczenie = get_object_or_404(Naliczenie_jeden_mieszkaniec, pk=my_id)
    if request.method == "POST":
        naliczenie.delete()
        return redirect(wszystkie_naliczenia_wlascicieli)
    return render(request, 'usun_naliczenie_wlasciciela.html', {'naliczenie': naliczenie, 'adres': adres})