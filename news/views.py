# -*- coding: utf-8 -*-
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.template import loader, Context
from django.http import HttpResponse
from django.core.context_processors import csrf

from blog.models import Entry
from .models import News


def newsarchive(request):
    posts = Entry.objects.all()
    news = News.objects.all()[:5]
    t = loader.get_template('news.html')
    ctx = { 'posts': posts , 'news': news, }
    ctx.update(csrf(request))
    c = Context(ctx)
    return HttpResponse(t.render(c))
