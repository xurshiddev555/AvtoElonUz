from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from avto import admin
from avto.views import UserListApiView, FilesListApiView, CharacterAutoApiListView, MeasureListApiView, \
    ParameterListApiView, ParametersItemListApiView, ElonCharacterListApiView, ElonFilesListApiView, CreateUserView, \
    UpdateUserView, DeleteUserView
from root import settings

urlpatterns = [
    path('user/', UserListApiView.as_view(), name='user-list'),
    path('files/', FilesListApiView.as_view(), name='files-list'),
    path('character-auto/', CharacterAutoApiListView.as_view(), name='character-auto'),
    path('measure-list/', MeasureListApiView.as_view(), name='measure-list'),
    path('parameter-list/', ParameterListApiView.as_view(), name='parameter-list'),
    path('parameter-item-list/', ParametersItemListApiView.as_view(), name='parameter-item-list'),
    path('character-elon/', ElonCharacterListApiView.as_view(), name='character-elon'),
    path('files-elon/', ElonFilesListApiView.as_view(), name='files-elon'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('update-user/', UpdateUserView.as_view(), name='update-user'),
    path('delete-user/', DeleteUserView.as_view(), name='delete-user'),
]

