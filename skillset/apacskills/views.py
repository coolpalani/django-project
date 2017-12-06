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

    def a(self):
        skill_list = Skills.objects.all()
        #return render(request, 'home.html', context={"skill_name": skill_list})
        return skill_list

    def get_lvda(self):
        lvda_skill_map = Skills_map.objects.filter(skill_name_id='LVDA')
        return lvda_skill_map
    def get_xs(self):
        xs_skill_map = Skills_map.objects.filter(skill_name_id='XenServer')
        return xs_skill_map

    def get_rfl(self):
        rfl_skill_map = Skills_map.objects.filter(skill_name_id='Receiver for Linux')
        return rfl_skill_map

    def get(self, request):
        skill_list=self.a()
        lvda_skill_map=self.get_lvda()
        xs_skill_map=self.get_xs()
        rfl_skill_map=self.get_rfl()
        return render(request, 'home.html', context={"skill_name": skill_list, "lvda_skill_list": lvda_skill_map, "xs_skill_list": xs_skill_map, "rfl_skill_list": rfl_skill_map })
    #productList = list()
    #for product_name in xs_skill:
    #    productList.append(product_name)
    #    xs_map_results = Skills_map.objects.filter(skill_name_id=product_name)

    #def get(self, request):
    #    skill_list=self.a()
        # Working   template_name: home-v1.html-----------------
        #tech_product_list = []

    #    xs_skill = Skills.objects.filter(skills__contains='XenServer')

        #productList = list()
    #    for product_name in xs_skill:
        #    productList.append(product_name)
    #        xs_map_results = Skills_map.objects.filter(skill_name_id=product_name)
        #for product in xs_skill:
        #xs_map_results = Skills_map.objects.values_list('user_id_id', 'skill_name_id')
        #xs_map_results = Skills_map.objects.values('user_id_id', 'skill_name_id', 'skill_level')

        #lvda_skill = Skills.objects.filter(skills = 'LVDA')
        #lvda_map_results = Skills_map.objects.filter(skill_name_id = 'LVDA')
        #return render(request, 'home.html', context={"xs_map_results": xs_map_results, "xs_skill_name": xs_skill, "lvda_map_results": lvda_map_results, "lvda_skill_name": lvda_skill})
    #    return render(request, 'home.html', context={"xs_map_results": xs_map_results, "skill_name": skill_list})
        #---------------------
    #def get(self, request):

    #    lva_skill = Skills.objects.filter(skills__contains='LVDA')
    #    for product_name in lva_skill:
    #        lvda_map_results =  Skills_map.objects.filter(skill_name_id=product_name)
    #    return render(request, 'home.html', context={"lvda_map_results": lvda_map_results})
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
