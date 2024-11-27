from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView

from avto.models import Users, Measure, CharacterAuto, Parameters, Files, ParametersItem, ElonCharacter, ElonFile
from avto.serializer import UsersSerializer, FileSerializer, MeasureSerializer, ParametersSerializer, \
    ParametersItemSerializer, ElonCharacterSerializer, ElonFileSerializer

@extend_schema(tags=['Users'])
class UserListApiView(ListAPIView):  # noqa
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Users.objects.all()

@extend_schema(tags=['CreateUser'])
class CreateUserView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        return Users.objects.create_user(data['username'], data['email'], data['password'])

@extend_schema(tags=['UpdateUser'])
class UpdateUserView(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_update(self, serializer):
        data = serializer.validated_data
        return Users.objects.update_user(data['username'], data['email'], data['password'])

@extend_schema(tags=['DeleteUser'])
class DeleteUserView(APIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def delete(self, request, *args, **kwargs):
        data = request.data
        if data['username']:
            del data['username', 'email', 'password']

@extend_schema(tags=['FilesListApi'])
class FilesListApiView(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Files.objects.all()

@extend_schema(tags=['CharactersListApi'])
class CharacterAutoApiListView(ListAPIView):
    queryset = CharacterAuto.objects.all()
    serializer_class = UsersSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return CharacterAuto.objects.all()

@extend_schema(tags=['MeasureListApi'])
class MeasureListApiView(ListAPIView):  # noqa
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Measure.objects.all()

@extend_schema(tags=['ParameterListApi'])
class ParameterListApiView(ListAPIView):  # noqa
    queryset = Parameters.objects.all()
    serializer_class = ParametersSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Parameters.objects.all()

@extend_schema(tags=['ParameterItemListApi'])
class ParametersItemListApiView(ListAPIView):
    queryset = Parameters.objects.all()
    serializer_class = ParametersItemSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ParametersItem.objects.all()

@extend_schema(tags=[''])
class ElonCharacterListApiView(ListAPIView):
    queryset = ElonCharacter.objects.all()
    serializer_class = ElonCharacterSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ElonCharacter.objects.all()

@extend_schema(tags=['ElonFileListApi'])
class ElonFilesListApiView(ListAPIView):
    queryset = ElonFile.objects.all()
    serializer_class = ElonFileSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return ElonFile.objects.all()
