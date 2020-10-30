from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from create_pdf_documents.forms import MieszkaniecForm
from view_s.wlasciciele import wlasciciele


@login_required
def nowy_wlasciciel(request):
    person = 0
    form = MieszkaniecForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(wlasciciele)
    return render(request, 'wlasciciel_formularz.html', {'form': form, 'person': person})