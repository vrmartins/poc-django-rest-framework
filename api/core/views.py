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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerByCNPJViewSet(APIView):

    def post(self, request, cnpj):
        if not cnpj_is_valid(cnpj):
            raise ValidationError("invalid cnpj")

        data = {
            'name': 'Sadio Mané',
            'address': 'Nigéria',
            'cnpj': cnpj
        }

        serializer = CustomerSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data['id'] = serializer.data['id']
        return Response(data)
