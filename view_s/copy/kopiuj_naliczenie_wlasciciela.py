from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from create_pdf_documents.forms import Naliczenie_jeden_mieszkaniecForm
from create_pdf_documents.models import Naliczenie_jeden_mieszkaniec
from view_s.wszystkie_naliczenia_wlascicieli import wszystkie_naliczenia_wlascicieli


@login_required
def kopiuj_naliczenie_wlasciciela(request, my_id):
    new = 2
    naliczenie = get_object_or_404(Naliczenie_jeden_mieszkaniec, pk=my_id)
    form = Naliczenie_jeden_mieszkaniecForm(request.POST or None, request.FILES or None, instance=naliczenie)
    naliczenie.pk = None
    if form.is_valid():
        form.save()
        return redirect(wszystkie_naliczenia_wlascicieli)
    return render(request, 'naliczenie_wlasciciel_formularz.html', {'form': form, 'new': new, 'naliczenie': naliczenie})