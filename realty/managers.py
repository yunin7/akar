# -*- coding: utf-8 -*-
from django.db.models.manager import Manager


class ManagerBase(Manager):
    def choices(self):
        result = [(0, u'Любой'),]
        result += list(self.values_list('pk', 'name'))
        return result


class TypeManager(ManagerBase):
    pass


class TownManager(ManagerBase):
    pass
