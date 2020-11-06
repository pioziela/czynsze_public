from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from create_pdf_documents.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('create_pdf_documents.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]