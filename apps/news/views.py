from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import News


class NewsListView(ListView):
    model = News
    paginate_by = 10


class NewsDetailView(DetailView):
    model = News
