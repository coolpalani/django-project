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
#from apacskills.homepagefunctions import Sumitview

# Create your views here.
#class ListSkillmap(DetailView, ListView):
#    model = Skills_map
#    context_object_name = 'found_map'
#    queryset = Skills_map.objects.all()
#    template_name = 'skills_map_list.html'


class skillmap(generic.ListView, View):

    def get(self, request):
        # Working   template_name: home-v1.html-----------------
        skill_list = Skills.objects.all()
        xs_skill = Skills.objects.filter(skills__in = skill_list)
        #for product in skill_list:
        xs_map_results = Skills_map.objects.filter(skill_name_id__in = skill_list)
        #lvda_skill = Skills.objects.filter(skills = 'LVDA')
        #lvda_map_results = Skills_map.objects.filter(skill_name_id = 'LVDA')
        #return render(request, 'home.html', context={"xs_map_results": xs_map_results, "xs_skill_name": xs_skill, "lvda_map_results": lvda_map_results, "lvda_skill_name": lvda_skill})
        return render(request, 'home.html', context={"xs_map_results": xs_map_results, "xs_skill_name": xs_skill})
        #---------------------

        # For loop
        #tech_product = ['XenServer','LVDA' ]
        #tech_product_list = []
        #for product in tech_product:
        #    xs_skill = Skills.objects.get(skills__contains = product)
        #    tech_product_list.append(xs_skill)
        #return render(request, 'home.html', context={"xs_skill_name": tech_product_list})
        #-------------------------




    #def get_queryset(self):
    #    return Skills_map.objects.filter(skill_name_id__contains = 'LVDA')
