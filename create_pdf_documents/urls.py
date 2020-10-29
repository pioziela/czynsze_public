from django.urls import path
from create_pdf_documents.views import index

urlpatterns = [
    path('index/', index),
]