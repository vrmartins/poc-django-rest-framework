# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .models import Customer
from .serializers import CustomerSerializer
from core.utils.cnpj_is_valid import cnpj_is_valid
from rest_framework.serializers import ValidationError
import requests


def get_address(city, village, address):
    result = 'Sem rua' if not address else address
    result += ' - '
    result += 'Sem bairro' if not village else village
    result += ' - '
    result += 'Sem cidade' if not city else city
    return result

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerByCNPJViewSet(APIView):

    def post(self, request, cnpj):
        # Como fazer um Promise.race ou Promise.all no python?
        response = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
        if not response.status_code == 200:
            raise EnvironmentError('Um erro ocorreu na integração')
        response_json = response.json()

        data = {
            'name': response_json['nome'],
            'address': get_address(city=response_json['municipio'], village=response_json['bairro'], address=response_json['logradouro']),
            'cnpj': cnpj
        }

        serializer = CustomerSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['id'] = serializer.data['id']
        return Response(data)
