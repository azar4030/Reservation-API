from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class RetrieveUserView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = get_user_model().Objects.all()
    lookup_field = 'email'


class ListUserView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = get_user_model().Objects.all()


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = get_user_model().Objects.all()
    lookup_field = 'email'


class DeleteUserView(generics.DestroyAPIView):
    queryset = get_user_model().Objects.all()
    lookup_field = 'email'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message':'user deleted successfully'},status.HTTP_200_OK,)

