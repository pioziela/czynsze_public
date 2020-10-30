from django.urls import path
from create_pdf_documents.views import index, nowa_wspolnota, nowy_wlasciciel, nowe_naliczenie_wspolnota,\
    nowe_naliczenie_wlasciciela, load_wspolnoty, wszystkie_wspolnoty, wszyscy_wlasciciele, wlasciciele, \
    wszystkie_naliczenia_wspolnot, wszystkie_naliczenia_wlascicieli, naliczenia, sortowanie_wlascicieli, \
    sortowanie_naliczen_wspolnot, sortowanie_naliczen_wlascicieli

urlpatterns = [
    path('index/', index),
    path('naliczenia/', naliczenia),
    path('nowa_wspolnota/', nowa_wspolnota),
    path('nowy_wlasciciel/', nowy_wlasciciel),
    path('nowe_naliczenie_wspolnota/', nowe_naliczenie_wspolnota),
    path('nowe_naliczenie_wlasciciela/', nowe_naliczenie_wlasciciela),
    path('ajax/load_wspolnoty', load_wspolnoty, name='ajax_load_wspolnoty'),
    path('wspolnoty/', wszystkie_wspolnoty),
    path('wspolnota/<int:my_id>/', wszyscy_wlasciciele),
    path('wlasciciele/', wlasciciele),
    path('naliczenia_wspolnot/', wszystkie_naliczenia_wspolnot),
    path('naliczenia_mieszkaniec/', wszystkie_naliczenia_wlascicieli),
    path('wlasciciele/order/<sorter>/', sortowanie_wlascicieli),
    path('naliczenia/wspolnoty/order/<sorter>/', sortowanie_naliczen_wspolnot),
    path('naliczenia/wlascicieli/order/<sorter>/', sortowanie_naliczen_wlascicieli),
]