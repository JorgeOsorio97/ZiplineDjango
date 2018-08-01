from django.db import models
from django.contrib.postgres.fields import JSONField

class Securities(models.Model):
    security = models.CharField(max_length =10, unique = True)
    name = models.CharField(max_length = 50, unique = True)
    market = models.CharField(max_length = 50)

    def __str__(self):
        return self.name + ", " + self.security

class Strategies(models.Model):
    security = models.CharField(max_length =50)
    strategy = JSONField()
    percentage_up = models.FloatField(default=None)
    last_modified = models.DateTimeField(auto_now = True )

    def __str__(self):
        return self.security + ',' + self.strategy    
