from django.db import models
from core.utils.cnpj_is_valid import cnpj_is_valid


class Customer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False, validators=[cnpj_is_valid])

    def __str__(self):
        return self.name
