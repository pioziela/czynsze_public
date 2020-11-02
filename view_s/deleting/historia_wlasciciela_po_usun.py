from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from create_pdf_documents.models import Mieszkaniec, Wspolnota


@login_required
def historia_wlasciciela_po_usun(request, my_id, numer_mieszkania):
    date = datetime.today().strftime("%Y-%m-%d")
    wspolnota = Wspolnota.objects.get(id=my_id)
    historia_mieszkanca = Mieszkaniec.objects.all().filter(wspolnota=wspolnota).filter(adres_numer_mieszkania=numer_mieszkania).order_by('-dane_od')
    if len(historia_mieszkanca) > 0:
        imie, nazwisko, wspolnota, adres_numer_mieszkania = historia_mieszkanca[0].imie, historia_mieszkanca[0].nazwisko, historia_mieszkanca[0].wspolnota, historia_mieszkanca[0].adres_numer_mieszkania
    else:
        return redirect(f'/wspolnota/{my_id}/')
    return render(request, 'historia_wlasciciela.html', {'date': date, 'historia': historia_mieszkanca, 'imie': imie, 'nazwisko': nazwisko, 'wspolnota': wspolnota, 'id': my_id})