from django.db import models
from ShowIndicators.models import Securities, Strategies

# Create your models here.
class Transaction(models.Model):
    id = models.AutoField(primary_key = True)
    stock_id = models.ForeignKey(Securities, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    stock_value = models.FloatField()
    date = models.DateTimeField()
    stratefy_used = models.ForeignKey(Strategies, on_delete=models.CASCADE)

    def __str__(self):
            return self.id