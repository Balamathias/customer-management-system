# Generated by Django 4.1.1 on 2022-10-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('out of delivery', 'out of delivery'), ('delivered', 'delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('indoor', 'indoor'), ('outdoor', 'outdoor')], max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
