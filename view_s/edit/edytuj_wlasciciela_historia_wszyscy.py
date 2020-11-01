from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import MieszkaniecForm
from create_pdf_documents.models import Wspolnota, Mieszkaniec


@login_required
def edytuj_wlasciciela_historia_wszyscy(request, my_id):
    person = 1
    wlasciciel = get_object_or_404(Mieszkaniec, pk=my_id)
    form = MieszkaniecForm(request.POST or None, request.FILES or None, instance=wlasciciel)
    mieszkaniec = Mieszkaniec.objects.get(id=my_id)
    wspolnota_mieszkanca = mieszkaniec.wspolnota
    wspolnota_id = Wspolnota.objects.get(wspolnota=wspolnota_mieszkanca).id
    if form.is_valid():
        form.save()
        return redirect(f'/historia/wspolnota/{wspolnota_id}/')
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person':person, 'wlasciciel': wlasciciel})