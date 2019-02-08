from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Securities, Strategies, Result
#from .models import Strategies
#from ShowIndicators.models import Securities, Strategies

# Register your models here.
@admin.register(Securities)
@admin.register(Strategies)
@admin.register(Result)
class SecuritiesAdmin(ImportExportModelAdmin):
    pass
class StrategiesAdmin(ImportExportModelAdmin):
    pass
class ResultAdmin(ImportExportModelAdmin):
    pass

