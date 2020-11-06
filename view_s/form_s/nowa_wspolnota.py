from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from create_pdf_documents.forms import WspolnotaForm
from view_s.wszystkie_wspolnoty import wszystkie_wspolnoty


@login_required
def nowa_wspolnota(request):
    form = WspolnotaForm(request.POST or None, request.FILES or None)
    association = 0
    if form.is_valid():
        form.save()
        return redirect(wszystkie_wspolnoty)
    return render(request, 'wspolnota_formularz.html', {'form': form, 'association': association})