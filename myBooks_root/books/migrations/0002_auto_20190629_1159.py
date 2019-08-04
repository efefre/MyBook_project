# Generated by Django 2.2.2 on 2019-06-29 09:59

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='averageRaiting',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0'), max_digits=3),
        ),
    ]