from rest_framework.serializers import ModelSerializer

from avto.models import Users, Files, CharacterAuto, Measure, Status, Parameters, ParametersItem, ElonFile, Type

class UsersSerializer(ModelSerializer):  # noqa
    class Meta:
        model = Users
        fields = '__all__'

class FileSerializer(ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'

class CharacterAutoSerializer(ModelSerializer):
    class Meta:
        model = CharacterAuto
        fields = '__all__'

class MeasureSerializer(ModelSerializer):
    class Meta:
        model = Measure
        fields = '__all__'

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ParametersSerializer(ModelSerializer):  # noqa
    class Meta:
        model = Parameters
        fields = '__all__'

class ParametersItemSerializer(ModelSerializer):
    class Meta:
        model = ParametersItem
        fields = '__all__'

class ElonCharacterSerializer(ModelSerializer):
    class Meta:
        model = CharacterAuto
        fields = '__all__'

class ElonFileSerializer(ModelSerializer):
    class Meta:
        model = ElonFile
        fields = '__all__'

class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'








