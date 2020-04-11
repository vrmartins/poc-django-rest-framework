from rest_framework.serializers import ValidationError
from validate_docbr import CNPJ

cnpj = CNPJ()


def cnpj_is_valid(value):
    if not cnpj.validate(value):
        raise ValidationError("invalid cnpj")
    return True
