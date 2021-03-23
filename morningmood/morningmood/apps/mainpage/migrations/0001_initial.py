# Generated by Django 3.1.7 on 2021-03-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cur_date', models.DateTimeField(max_length=50, verbose_name='Date')),
                ('btc', models.CharField(max_length=20, verbose_name='BTC')),
                ('eth', models.CharField(max_length=20, verbose_name='ETH')),
                ('index', models.IntegerField(verbose_name='Index')),
                ('temperature', models.CharField(max_length=10, verbose_name='Temperature')),
                ('weather', models.CharField(max_length=300, verbose_name='Weather')),
                ('fortune', models.CharField(max_length=200, verbose_name='Fortune')),
            ],
        ),
    ]