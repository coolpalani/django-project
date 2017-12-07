# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from apacskills.models import Ctxapacusers, Skills, Skills_map
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.views import View

class skillmap(generic.ListView, View):
    def get(self, request):
        skill_list = Skills.objects.all()
        dict_cl={}
        for q in skill_list:
            dict_cl[q.skills]=Skills_map.objects.filter(skill_name_id=q.skills)
        return render(request, 'home.html', context={"skill_name":skill_list,"dict_cl":dict_cl  })
