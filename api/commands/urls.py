from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.commands.views import (pdf_generate_view,
                                CommandCreateViewSet)


router = DefaultRouter()
router.register('pdf-generate', CommandCreateViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('generate-command/', pdf_generate_view),
]
