from django.http import HttpResponse
from .resources import securitiesResource

def export(request):
    securities_resource = securitiesResource()
    dataset = securities_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response