from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from create_pdf_documents.models import Mieszkaniec


@login_required
def load_wspolnoty(request):
    date = str(datetime.today().strftime("%Y-%m-%d"))
    wspolnota_id = request.GET.get('wspolnota_id')
    mieszkaniec = Mieszkaniec.objects.filter(wspolnota_id=wspolnota_id).filter(dane_do__gte=date)
    return render(request, 'wlasciciele_dana_wspolnota.html', {'mieszkaniec':mieszkaniec})