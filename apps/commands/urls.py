from django.urls import path

from .views import pdf_generate_view


urlpatterns = [
    path('pdf-generate/', pdf_generate_view),
]
