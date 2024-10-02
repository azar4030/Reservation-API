from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='creat'),
    path('get/<str:email>', RetrieveUserView.as_view(), name='get'),
    path('list/', ListUserView.as_view(), name='list'),
    path('update/<str:email>', UpdateUserView.as_view(), name='update'),
    path('delete/<str:email>', DeleteUserView.as_view(), name='delete')
]
