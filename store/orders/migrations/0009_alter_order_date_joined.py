# Generated by Django 4.2 on 2023-06-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_total_alter_order_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_joined',
            field=models.CharField(default='06/04/2023, 21:45:32', max_length=1000),
        ),
    ]
