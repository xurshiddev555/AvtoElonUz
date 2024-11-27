from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from avto.views import UserListApiView, FilesListApiView, CharacterAutoApiListView, MeasureListApiView, \
    ParameterListApiView, ParametersItemListApiView, ElonCharacterListApiView, ElonFilesListApiView, CreateUserView, \
    UpdateUserView, DeleteUserView
from root import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('avto.urls')),
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
