from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from create_pdf_documents.models import Mieszkaniec
from view_s.wlasciciele import wlasciciele


@login_required
def usun_wlasciciela(request, my_id):
    adres = f'/wlasciciele/'
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    if request.method == "POST":
        wlasciciel.delete()
        return redirect(wlasciciele)
    return render(request, 'usun_wlasciciela.html', {'wlasciciel': wlasciciel, 'adres': adres})