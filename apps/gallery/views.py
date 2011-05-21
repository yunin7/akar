from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from models import Gallery


class GalleryListView(ListView):
    model = Gallery


class GalleryDetailView(DetailView):
    model = Gallery
