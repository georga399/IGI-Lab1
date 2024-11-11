# Generated by Django 5.0.6 on 2024-06-05 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('hotelinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promoinstance',
            name='promo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelinfo.promo'),
        ),
        migrations.AddField(
            model_name='client',
            name='promos',
            field=models.ManyToManyField(through='accounts.PromoInstance', to='hotelinfo.promo'),
        ),
    ]
