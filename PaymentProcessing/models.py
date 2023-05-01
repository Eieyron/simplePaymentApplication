from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.

class Currency(models.Model):

    name = models.CharField(max_length = 150)
    code = models.CharField(unique=True, max_length = 150)
    created_date = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def save(self, *args, **kwargs):

        self.created_date = datetime.now()

        return super().save(*args, **kwargs)


class Payment(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reference_code = models.CharField(unique=True, max_length = 150)
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    created_date = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.get_username() + '-' + self.reference_code

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def save(self, *args, **kwargs):

        self.created_date = datetime.now()

        if self.is_paid:
            self.paid_date = datetime.today()

        return super().save(*args, **kwargs)