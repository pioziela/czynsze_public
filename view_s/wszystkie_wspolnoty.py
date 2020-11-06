from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from create_pdf_documents.models import Wspolnota


@login_required
def wszystkie_wspolnoty(request):
    date = datetime.today().strftime("%Y-%m-%d")
    wszystkie = Wspolnota.objects.order_by('wspolnota')
    return render(request, 'wszystkie_wspolnoty.html', {'all': wszystkie, 'date': date})