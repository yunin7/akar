from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import News


class NewsListView(ListView):
    model = News


class NewsDetailView(DetailView):
    model = News
