from django.urls import path, include, re_path
from rest_framework import routers

from .views import PaymentView, CurrencyView

router = routers.DefaultRouter()
router.register('payments', PaymentView, basename='payment')
router.register('currencys', CurrencyView, basename='currency')

urlpatterns = router.urls