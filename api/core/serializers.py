from rest_framework import serializers
from .models import Customer

def get_info_by_cnpj(cnpj):
    return {
        'name': 'blabla',
        'address': 'blabla address'
    }

def has_all_fields(customer):
    if customer['name'] and customer['address']:
        return True
    return False

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'cnpj')
