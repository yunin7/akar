# -*- coding: utf-8 -*-
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from realty.forms import SearchForm
from realty.models import Property


class PropertyListView(ListView):
    model = Property

    def get(self, request, *args, **kwargs):
        filter = kwargs
        form = SearchForm(request.GET)
        filter.update(form.filter())
        self.object_list = self.get_queryset().filter(**filter)
        context = self.get_context_data(
            object_list=self.object_list,
            kwargs=kwargs
        )
        return self.render_to_response(context)


class PropertyDetailView(DetailView):
    model = Property
