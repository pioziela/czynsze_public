from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Naliczenie_cala_wspolnota
from view_s.wszystkie_naliczenia_wspolnot import wszystkie_naliczenia_wspolnot


@login_required
def usun_naliczenie_wspolnoty(request, my_id):
    naliczenie = get_object_or_404(Naliczenie_cala_wspolnota, pk=my_id)
    adres = f'/naliczenia_wspolnot/'
    if request.method == "POST":
        naliczenie.delete()
        return redirect(wszystkie_naliczenia_wspolnot)
    return render(request, 'usun_naliczenie_wspolnoty.html', {'naliczenie': naliczenie, 'adres': adres})