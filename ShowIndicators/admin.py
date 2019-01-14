from django.contrib import admin
from ShowIndicators.models import Securities, Strategies, Result

# Register your models here.
admin.site.register(Securities)
admin.site.register(Strategies)
admin.site.register(Result)