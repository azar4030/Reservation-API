from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('crud', ClinicViewSet, basename='crud')

app_name = 'clinic'

urlpatterns = [

    path('', include(router.urls)),
]
