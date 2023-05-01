from rest_framework import serializers
from django.db.models import Sum
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from .models import Payment, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):

        # custom create that
        # 1) lets user create payment up to 5000 per currency per day
        # 2) if error, return error

        temp_created_date = datetime.today()

        # check if user's total for the day in payment in the selected currency is less than 5000
        user_total_payment = Payment.objects.filter(**{
            'user':validated_data['user'],
            'currency':validated_data['currency'],
        }).filter(created_date__gt=temp_created_date-timedelta(days=1), created_date__lte=temp_created_date).aggregate(Sum('amount'))['amount__sum'] or 0

        print("user total payment", user_total_payment)

        if (user_total_payment+validated_data['amount']) > 5000:
            raise serializers.ValidationError({
                "Currency Payment Limit Reached": "must be less than 5000 within the day"
            })

        return super().create(validated_data)

