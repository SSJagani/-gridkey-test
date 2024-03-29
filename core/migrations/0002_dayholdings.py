# Generated by Django 4.2.2 on 2023-06-16 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayHoldings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('balance_qty', models.IntegerField(default=0)),
                ('total_cost_price', models.DecimalField(decimal_places=2, default='0.00', max_digits=10)),
            ],
            options={
                'verbose_name': 'DayHoldings',
                'verbose_name_plural': 'DayHoldings',
                'db_table': 'day_holdings',
                'indexes': [models.Index(fields=['id'], name='day_holding_id_3410e9_idx'), models.Index(fields=['created_at'], name='day_holding_created_4b73d6_idx')],
            },
        ),
    ]
