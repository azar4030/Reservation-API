from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import *
# Create your views here.


class ClinicViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()

