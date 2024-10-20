from django.urls import path
from django.urls import include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from .viewset import SalaViewSet

router = DefaultRouter()

router.register('salas', SalaViewSet, 'salas')

urlpatterns = [
  path('', include(router.urls)),
  path('docs/', include_docs_urls(title='Salas Informatica API'))
]