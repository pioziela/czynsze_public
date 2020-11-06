from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Mieszkaniec, Wspolnota


@login_required
def usun_wlasciciela_historia(request, my_id):
    mieszkaniec = Mieszkaniec.objects.get(id=my_id)
    imie, nazwisko, wspolnota, adres_numer_mieszkania = mieszkaniec.imie, mieszkaniec.nazwisko, mieszkaniec.wspolnota, mieszkaniec.adres_numer_mieszkania
    id_wspolonty = Wspolnota.objects.get(wspolnota=wspolnota).id
    adres = f'/historia_wlasciciela/{id_wspolonty}/{adres_numer_mieszkania}/'
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    if request.method == "POST":
        wlasciciel.delete()
        return redirect(f'/historia_wlasciciela/{id_wspolonty}/{adres_numer_mieszkania}/')
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})