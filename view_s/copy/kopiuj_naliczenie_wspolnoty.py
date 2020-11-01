from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import Naliczenie_cala_wspolnotaForm
from create_pdf_documents.models import Naliczenie_cala_wspolnota
from view_s.wszystkie_naliczenia_wspolnot import wszystkie_naliczenia_wspolnot


@login_required
def kopiuj_naliczenie_wspolnoty(request, my_id):
    new = 2
    naliczenie = get_object_or_404(Naliczenie_cala_wspolnota, pk=my_id)
    form = Naliczenie_cala_wspolnotaForm(request.POST or None, request.FILES or None, instance=naliczenie)
    naliczenie.pk = None
    if form.is_valid():
        form.save()
        return redirect(wszystkie_naliczenia_wspolnot)
    return render(request, 'naliczenie_wspolnota_formularz.html', {'form': form, 'new': new, 'naliczenie': naliczenie})