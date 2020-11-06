from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def usun_wlasciciela_historia_wszyscy(request, my_id):
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    mieszkaniec = Mieszkaniec.objects.get(id=my_id)
    wspolnota_mieszkanca = mieszkaniec.wspolnota
    wspolnota_id = Wspolnota.objects.get(wspolnota=wspolnota_mieszkanca).id
    adres = f'/historia/wspolnota/{wspolnota_id}/'
    if request.method == "POST":
        wlasciciel.delete()
        return redirect(f'/historia/wspolnota/{wspolnota_id}/')
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})