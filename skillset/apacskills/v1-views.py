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


#def homepage(request):
#    employees=User.objects.all()
#    employees = Employees.objects.all()
#    emp = employees.filter(user_id="sumitka")
#    return render(request, 'home.html', context={'employees':employees},
#    )

#class UserList(ListView):
#    model = Ctxapacusers
#    template_name = 'home.html'
#    def get_context_data(self, **kwargs):
#        # Call the base implementation first to get a context
#        context = super(UserList, self).get_context_data(**kwargs)
#        # Get the blog from id and add it to the context
#        context['some_data'] = 'This is just some data'
#        return context

#def skillmap(request):
    #emp_name = Ctxapacusers.objects.get(skills='XenServer')

#    db_skill_name = Skills.objects.get(skills="XenServer")
#    return render(request, 'home.html', context={'skill_name':db_skill_name})

class skillmap(generic.ListView, View):


    #def get(self, request):
    #    skill = Skills.objects.filter(skills__contains='XenServer')
    #    return render(request, 'home.html', context={"xs_skill_name": skill})

    def get(self, request):
        tech_product = ['XenServer', 'LVDA' ]
        tech_product_list = []
        product_map = []
        for product in tech_product:
            xs_skill = Skills.objects.filter(skills__contains=product)
            tech_product_list.append(xs_skill)
            xs_map_results = Skills_map.objects.filter(skill_name_id__in = product)
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

    #def get_context_data(self, **kwargs):
    #    tech_product = ['XenServer', 'LVDA']
    #    for find_mapping in tech_product:
    #        context = super(skillmap, self).get_context_data(**kwargs)
    #        context['map_results'] = self.Skills_map.objects.filter(skill_name_id=find_mapping)
    #        return context

    #def get_queryset(self):
    #    tech_product = ['XenServer', 'LVDA']
    #    for find_mapping in tech_product:
    #        self.map_results = get.object(find_mapping, name=self.args[0])
    #        return Skills_map.objects.filter(map_results=self.map_results)


        #product_skill = Skills.objects.all()
        #find_mapping = []
        #for input_skill in product_skill:
            #map_results = Skills_map.objects.all()[:1]
            #skill_name = Skills.objects.get(skills="input_skill")
            #map_results = Skills_map.objects.filter(skill_name_id__in = Skills.objects.all())
            #find_mapping.append(map_results)
        #    return render(request, 'home.html', context={"skill_name": input_skill})
        #for tech_skill in skill:





#class skillmap(ListView):
#    model = Skills
#    def get_context_data(self, **kwargs):
#       context = super(skillmap, self).get_context_data(**kwargs)
#        context['skill_map'] =  'testing'
#        return context
#    #    skill_name = db_skill.filter(skills="XenServer")
#        return render(request, 'home.html', context={'skill_name':db_skill_name})

#    model = Skills_map
#    skill_map_user = Skills_map.objects.filter(skill_name="XenServer")
#    template_name = 'home.html'



#class skillmap(SingleObjectMixin, ListView):
#    paginate_by = 2
#    template_name = 'home.html'
#
#    def get(self, request, *args, **kwargs):
#        self.object = self.get_object(queryset=Skills_map.object.all())
#        return super().get(request, *args, **kwargs)

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['Skill Set view'] = self.object
#        return context

#    def get_queryset(self):
#        return self.object.skills_set.all()
