from django.urls import path, include
from tempo_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('leituras', views.LeituraViewSet)

urlpatterns = [
    path('', include(router.urls))
]
