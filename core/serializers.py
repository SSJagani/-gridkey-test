from datetime import date
from rest_framework import serializers
from .models import Transaction, DayHoldings


class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.DateField(default=date.today())

    class Meta:
        model = Transaction
        fields = '__all__'


class DayHoldingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayHoldings
        fields = '__all__'