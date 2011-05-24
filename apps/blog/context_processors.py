from models import Entry


def latest(request):
    '''5 latest news'''
    return {'last_entries': Entry.objects.all()[:5]}