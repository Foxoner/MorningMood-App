from django.db import models


class Information(models.Model):
    cur_date = models.DateTimeField('Date', max_length=50)  # Current Date
    btc = models.CharField('BTC', max_length=20)  # CryptoCurrency Rate
    eth = models.CharField('ETH', max_length=20)
    index = models.IntegerField('Index')  # Index BTC
    temperature = models.CharField('Temperature', max_length=10)  # Weather
    weather = models.CharField('Weather', max_length=300)
    fortune = models.CharField('Fortune', max_length=200)  # Daily Fortune

    def __str__(self):
        pass
