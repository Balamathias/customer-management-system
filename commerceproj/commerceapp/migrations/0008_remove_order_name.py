# Generated by Django 4.1.1 on 2022-10-06 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commerceapp', '0007_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
