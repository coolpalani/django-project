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


class skillmap(generic.ListView, View):


    #def get(self, request):
    #    skill = Skills.objects.filter(skills__contains='XenServer')
    #    return render(request, 'home.html', context={"xs_skill_name": skill})

    def get(self, request):
        tech_product = ['XenServer','LVDA' ]
        tech_product_list = []
        product_map = []
        for product in tech_product:
            xs_skill = Skills.objects.get(skills__contains=product)
            tech_product_list.append(xs_skill)
            xs_map_results = Skills_map.objects.filter(skill_name_id= product)
            product_map.append(xs_map_results)
        return render(request, 'home.html', context={"xs_map_results": product_map, "xs_skill_name": tech_product_list})
        #    return render(request, 'home.html', context={"xs_skill_name": tech_product_list})
        # Working-----------------
        #xs_skill = Skills.objects.get(skills__contains="XenServer")
        #xs_map_results = Skills_map.objects.filter(skill_name_id="XenServer")
        #lvda_skill = Skills.objects.get(skills="LVDA")
        #lvda_map_results = Skills_map.objects.filter(skill_name_id="LVDA")
        #return render(request, 'home.html', context={"xs_map_results": xs_map_results, "xs_skill_name": xs_skill, "lvda_map_results": lvda_map_results, "lvda_skill_name": lvda_skill})
        #---------------------
