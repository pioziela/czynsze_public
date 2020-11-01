from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def historia_wlasciciela(request, my_id):
    date = datetime.today().strftime("%Y-%m-%d")
    mieszkaniec = Mieszkaniec.objects.get(id=my_id)
    imie, nazwisko, wspolnota, adres_numer_mieszkania = mieszkaniec.imie, mieszkaniec.nazwisko, mieszkaniec.wspolnota, mieszkaniec.adres_numer_mieszkania
    historia_mieszkanca = Mieszkaniec.objects.all().filter(wspolnota=wspolnota, adres_numer_mieszkania=adres_numer_mieszkania).order_by('-dane_od')
    id_wspolonty = Wspolnota.objects.get(wspolnota=wspolnota)
    id = id_wspolonty.id
    return render(request, 'historia_wlasciciela.html', {'date': date, 'historia': historia_mieszkanca, 'imie': imie, 'nazwisko': nazwisko, 'wspolnota': wspolnota, 'id': id})