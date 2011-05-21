from django.template import loader, Context
from django.http import HttpResponse
from django.contrib.auth.models import User

from blog.models import Entry, Gals
from news.models import News


def archive(request):
    users = User.objects.all()
    posts = Entry.objects.all()
    news = News.objects.all()[:5]
    gals = Gals.objects.all()
    t = loader.get_template('archive.html')
    ctx = { 'posts': posts , 'news': news, 'users' : users, 'gals' : gals,}
    c = Context(ctx)
    return HttpResponse(t.render(c))

def blogitem(request, idblog):
    users = User.objects.all()
    posts = Entry.objects.filter(id=idblog)
    news = News.objects.all()[:5]
    t = loader.get_template('archive.html')
    ctx = { 'posts': posts , 'news': news, 'users' : users}
    c = Context(ctx)
    return HttpResponse(t.render(c))
