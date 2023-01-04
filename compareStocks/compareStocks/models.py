from django.db import models

class Security(models.Model):
    name = models.CharField(max_length = 100)
    prev_close = models.CharField(max_length = 100)
    pe_ratio = models.FloatField()
    dividend_yield = models.CharField(max_length = 100)
    primary_exchange = models.CharField(max_length = 100)
