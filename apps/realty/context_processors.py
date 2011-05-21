from models import Town, Type
from forms import SearchForm

def search_form(request):
    form = SearchForm(initial=(request.GET or {}))
    return {'search_form': form}

def towns(request):
    return {'towns': Town.objects.all()}

def types(request):
    return {'types': Type.objects.all()}