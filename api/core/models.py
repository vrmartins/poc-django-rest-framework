from django.db import models
from rest_framework.serializers import ValidationError
from validate_docbr import CNPJ

cnpj = CNPJ()


def cnpj_is_valid(value):
    if not cnpj.validate(value):
        raise ValidationError("invalid cnpj")


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False, validators=[cnpj_is_valid])

    def __str__(self):
        return self.name
