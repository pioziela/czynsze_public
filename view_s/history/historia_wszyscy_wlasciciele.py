from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def historia_wszyscy_wlasciciele(request, my_id):
    date = datetime.today().strftime("%Y-%m-%d")
    wszyscy_historia = Mieszkaniec.objects.all().filter(wspolnota=my_id).order_by('adres_numer_mieszkania', '-dane_od')
    wspolnota = Wspolnota.objects.get(id=my_id)
    return render(request, 'historia_wszyscy_wlasciciele.html', {'date': date, 'wszyscy_historia': wszyscy_historia, 'wspolnota': wspolnota, 'id': my_id})