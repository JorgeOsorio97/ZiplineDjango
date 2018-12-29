from django.db import models
from django.contrib.postgres.fields import JSONField

class Securities(models.Model):
    id = models.AutoField(primary_key = True)
    security = models.CharField(max_length =10, unique = True)
    name = models.CharField(max_length = 50)
    market = models.CharField(max_length = 50)
    stocks_own = models.IntegerField(null=True)
    providers_name = JSONField(null=True)
    csv_file = models.CharField(max_length =50, null=True)
    last_update = models.DateField(auto_now=True)  


    def __str__(self):
        return self.name + " - " + self.security
        
class Strategies(models.Model):
    id = models.AutoField(primary_key = True)
    security = models.CharField(max_length = 50)
    strategy = JSONField()                      
    percentage_up = models.FloatField(default=None)
    last_modified = models.DateTimeField(auto_now = True )
    max_point = models.FloatField(null=True)  
    min_point = models.FloatField(null=True)
    trades = models.IntegerField(null=True)

    
    def __str__(self):
        return self.security + ',' + self.id   
