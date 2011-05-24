from models import News


def latest(request):
    '''5 latest news'''
    return {'last_news': News.objects.all()[:5]}