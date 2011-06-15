from models import Town, Type, Property
from forms import SearchForm


def search_form(request):
    form = SearchForm(initial=(request.GET or {}))
    return {'search_form': form}

def towns(request):
    return {'towns': Town.objects.all()}

def types(request):
    return {'types': Type.objects.all()}

def shifting_properties(request):
    return {'shifting_properties': Property.objects.filter(
        show_on_home=True).order_by('?')[:5]}