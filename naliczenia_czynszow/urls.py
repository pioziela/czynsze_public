from django.contrib import admin
from django.urls import path
from czynsze_public.create_pdf_documents.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
]