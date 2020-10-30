from django.urls import path
from create_pdf_documents.views import index, nowa_wspolnota, nowy_wlasciciel, nowe_naliczenie_wspolnota,\
    nowe_naliczenie_wlasciciela

urlpatterns = [
    path('index/', index),
    path('nowa_wspolnota/', nowa_wspolnota),
    path('nowy_wlasciciel/', nowy_wlasciciel),
    path('nowe_naliczenie_wspolnota/', nowe_naliczenie_wspolnota),
    path('nowe_naliczenie_wlasciciela/', nowe_naliczenie_wlasciciela),
]