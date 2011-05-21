from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Entry


class EntryListView(ListView):
    model = Entry


class EntryDetailView(DetailView):
    model = Entry
