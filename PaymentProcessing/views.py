
from .models import Payment, Currency
from .serializers import PaymentSerializer, CurrencySerializer
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

import django_filters

# Create your views here.
class PaymentView(viewsets.ModelViewSet):

    '''
        This View Class Handles CRUD for the Payment Model
    '''

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reference_code', 'currency']


class CurrencyView(viewsets.ModelViewSet):

    '''
        This View Class Handles CRUD for the Currency Model
    '''

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [AllowAny]
