# -*- coding: utf-8 -*-
# News application
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.template import loader, Context
from django.http import HttpResponse
from django.core.context_processors import csrf
from blog.models import BlogPost, PostNews

def newsarchive(request):
  posts = BlogPost.objects.all()
  news = PostNews.objects.all()[:5]
  t = loader.get_template('news.html')
  ctx = { 'posts': posts , 'news': news, }
  ctx.update(csrf(request))
  c = Context(ctx)
  return HttpResponse(t.render(c))
