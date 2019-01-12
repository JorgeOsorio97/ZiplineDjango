from import_export import resources
from .models import Securities

class securitiesResource(resources.ModelResource):
    class Meta:
        model = Securities