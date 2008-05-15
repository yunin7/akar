# Blog Application
from django.template import loader, Context
from django.http import HttpResponse
from django.core.context_processors import csrf
from blog.models import BlogPost, PostNews, Gals
from django.contrib.auth.models import User
from registration import *

def archive(request):
  users = User.objects.all()
  posts = BlogPost.objects.all()
  news = PostNews.objects.all()[:5]
  gals = Gals.objects.all()
  t = loader.get_template('archive.html')
  ctx = { 'posts': posts , 'news': news, 'users' : users, 'gals' : gals,}
  ctx.update(csrf(request))
  c = Context(ctx)
  return HttpResponse(t.render(c))

def blogitem(request, idblog):
  users = User.objects.all()
#  posts = BlogPost.objects.get(id=idblog)
  posts = BlogPost.objects.filter(id=idblog)
  news = PostNews.objects.all()[:5]
  t = loader.get_template('archive.html')
  ctx = { 'posts': posts , 'news': news, 'users' : users}
  ctx.update(csrf(request))
  c = Context(ctx)
  return HttpResponse(t.render(c))
  
