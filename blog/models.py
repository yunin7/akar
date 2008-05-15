# Blog Application
from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User

class BlogPost(models.Model):
  title = models.CharField(max_length=150)
  short_text =  models.TextField()
  body = models.TextField()
  timestamp = models.DateTimeField()
  logo = models.ImageField(upload_to='blog/')
  class Meta: 
    ordering = ('-timestamp',)

class Gals(models.Model):
  title = models.CharField(max_length=150)
  imagef = models.ForeignKey(BlogPost)
  itemgal = models.ImageField(upload_to='blog/')

class GalsInLine(admin.TabularInline):
  model = Gals
  extra = 1
    
class BlogPostAdmin(admin.ModelAdmin):
  inlines = [
    GalsInLine,
  ]
  list_display = ('title', 'short_text', 'timestamp')
  list_display_links = ('title', 'short_text')
  
class PostNews(models.Model):
  title = models.CharField(max_length=150)
  short_text =  models.TextField()
  body = models.TextField()
  timestamp = models.DateTimeField()
  logo = models.ImageField(upload_to='news/')
  class Meta: 
    ordering = ('-timestamp',)

class NewsAdmin(admin.ModelAdmin):
  list_display = ('id', 'short_text', 'title', 'timestamp')

  
# Register BlogPost in model admin
admin.site.register(BlogPost, BlogPostAdmin) 
admin.site.register(PostNews, NewsAdmin) 
