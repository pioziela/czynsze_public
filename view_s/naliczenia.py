from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def naliczenia(request):
    return render(request, 'naliczenia.html')