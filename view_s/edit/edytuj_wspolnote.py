from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import WspolnotaForm
from create_pdf_documents.models import Wspolnota
from view_s.wszystkie_wspolnoty import wszystkie_wspolnoty


@login_required
def edytuj_wspolnote(request, my_id):
    wspolnota = get_object_or_404(Wspolnota, pk=my_id)
    association = 1
    form = WspolnotaForm(request.POST or None, request.FILES or None, instance=wspolnota)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_wspolnoty)
    return render(request, 'wspolnota_formularz.html', {'form': form, 'association': association, 'wspolnota': wspolnota})