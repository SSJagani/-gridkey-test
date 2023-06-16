from datetime import date
from copy import deepcopy
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Transaction(TimeStampedModel):
    TRADE_TYPES = (
        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
        ('SPLIT', 'SPLIT'),
    )
    date = models.DateField(db_index=True)
    company = models.CharField(max_length=100, db_index=True)
    trade_type = models.CharField(max_length=10, choices=TRADE_TYPES, db_index=True)
    quantity = models.IntegerField()
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.company} - {self.trade_type}"

    class Meta:
        db_table = "transaction"
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        indexes = [
            models.Index(fields=['id']),
        ]


class DayHoldings(TimeStampedModel):
    balance_qty = models.IntegerField(default=0)
    total_cost_price = models.DecimalField(decimal_places=2, max_digits=10, default="0.00")

    class Meta:
        db_table = "day_holdings"
        verbose_name = "DayHoldings"
        verbose_name_plural = "DayHoldings"
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['created_at']),
        ]


def calculate_avg_buy_price(sender, instance, created, *arg, **kwargs):
    transactions_qry = Transaction.objects.values('trade_type', 'quantity', 'price_per_share')
    transactions_list = deepcopy(transactions_qry.filter(trade_type='BUY'))
    for transaction in transactions_qry:
        if transaction['trade_type'] == 'SELL':
            transactions_list = sell_stock(transactions_list, transaction['quantity'])
        elif transaction['trade_type'] == 'SPLIT':
            transactions_list = split_stock(transactions_list, transaction['quantity'])
    balance_qty = 0
    total_cost_price = 0
    for transaction in transactions_list:
        if transaction['quantity'] > 0:
            balance_qty = balance_qty+transaction['quantity']
            total_cost_price = total_cost_price+(transaction['price_per_share']*transaction['quantity'])
    holding, created = DayHoldings.objects.get_or_create(created_at__date=date.today())
    holding.balance_qty = balance_qty
    holding.total_cost_price = total_cost_price/balance_qty
    holding.save()
    return True


def sell_stock(transactions_list, sell_quantity):
    for transaction in transactions_list:
        if transaction['trade_type'] == 'BUY':
            if transaction['quantity'] > 0 and transaction['quantity'] > sell_quantity:
                transaction['quantity'] = transaction['quantity']-sell_quantity
                break
            else:
                sell_quantity = sell_quantity-transaction['quantity']
                transaction['quantity'] = 0

    return transactions_list


def split_stock(transactions_list, number_of_stock):
    for transaction in transactions_list:
        transaction['quantity'] = transaction['quantity']*number_of_stock
        transaction['price_per_share'] = transaction['price_per_share']/number_of_stock
    return transactions_list


post_save.connect(calculate_avg_buy_price, sender=Transaction)
