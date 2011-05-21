from news.models import News

def latest(request):
    '''5 latest news'''
    return {'news': News.objects.all()[:5]}