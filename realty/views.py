# -*- coding: utf-8 -*-
# Object Application
# (c) Yunin Ivan yunin7@inbox.ru 2011

from django.template import loader, Context
from django.http import HttpResponse
from django.core.context_processors import csrf

from realty.models import RealObject, Gals


def realty(request):
    realty = RealObject.objects.all()
    gals = Gals.objects.all()
    t = loader.get_template('realty.html')
    ctx = { 'realty': realty, 'gals': gals,}
    ctx.update(csrf(request))
    c = Context(ctx)
    return HttpResponse(t.render(c))
