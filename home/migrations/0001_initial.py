# Generated by Django 3.2.18 on 2023-05-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=3)),
                ('country', models.CharField(max_length=50)),
                ('purchase_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
    ]
