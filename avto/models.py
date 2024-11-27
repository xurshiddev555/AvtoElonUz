from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE, TextChoices


class Files(Model):
    url = CharField(max_length=255, unique=True)


class Measure(Model):
    name = CharField(max_length=255)
    short_name = CharField(max_length=255, null=True, blank=True)


class Parameters(Model):
    name = CharField(max_length=255)
    measure_id = ForeignKey('avto.Measure', on_delete=CASCADE)


class ParametersItem(Model):
    name = CharField(max_length=255)
    parameter_id = ForeignKey('avto.Parameters', on_delete=CASCADE)
    value = CharField(max_length=255)
    file_id = ForeignKey('avto.Files', on_delete=CASCADE)


class Users(Model):
    name = CharField(max_length=255)
    phone_number = CharField(max_length=255, null=True, blank=True)
    photo_id = ForeignKey('avto.Files', on_delete=CASCADE)


class CharacterAuto(Model):
    user_id = ForeignKey('avto.Users', on_delete=CASCADE)
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    status = CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class ElonCharacter(Model):
    elon_id = ForeignKey('avto.CharacterAuto', on_delete=CASCADE)
    parameters_id = ForeignKey('avto.Parameters', on_delete=CASCADE)
    parameters_item_id = ForeignKey('avto.ParametersItem', on_delete=CASCADE)
    parameters_value = CharField(max_length=255, null=True, blank=True)


class ElonFile(Model):
    elon_id = ForeignKey('avto.ElonCharacter', on_delete=CASCADE)
    file_id = ForeignKey('avto.Files', on_delete=CASCADE)


class Type(Model):
    name = CharField(max_length=255)
    code = CharField(max_length=255)
    type_id = ForeignKey('avto.Parameters', on_delete=CASCADE)


class Status(Model):
    class Type(TextChoices):
        KUTILMOQDA = 'kutilmoqda', 'Kutilmoqda'

    name = CharField(max_length=255)
    type = CharField(choices=Type.choices, max_length=255, default=Type.KUTILMOQDA)
    code = CharField(max_length=255)
