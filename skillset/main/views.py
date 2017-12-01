# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from main.models import Employees
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
# Create your views here.
#def home(request):
#    return HttpResponse("Hello World!")

#def home(request):
#    return render(request, "main/home.html", {'message': 'hi, sumit'})

def homepage(request):
#    employees=User.objects.all()
    employees = Employees.objects.all()
#    emp = employees.filter(user_id="sumitka")
    return render(request, 'home.html', context={'employees':employees},
    )

class UserList(ListView):
    model = Employees
    template_name = 'home.html'
#    def get_context_data(self, **kwargs):
#        # Call the base implementation first to get a context
#        context = super(UserList, self).get_context_data(**kwargs)
#        # Get the blog from id and add it to the context
#        context['some_data'] = 'This is just some data'
#        return context

def index(request):
    homepage = Employees.objects.all()
    return render(request, 'index.html', {'homepage': homepage})

# Add the two views we have been talking about  all this time :)
#class HomePageView(TemplateView):
#    template_name = "home.html"



class UserCreateView(generic.CreateView):
    from_class = UserCreationForm
    model = User
    template_name = 'createuser.html'
#    def __init__(self, arg):
#        super(UserCreateView, self).__init__()
#        self.arg = arg


class AboutPageView(TemplateView):
    template_name = "about.html"

# Add this view
class DataPageView(TemplateView):
    def get(self, request, **kwargs):
        # we will pass this context object into the
        # template so that we can access the data
        # list in the template
        context = {
            'data': [
                {
                    'name': 'Celeb 1',
                    'worth': '3567892'
                },
                {
                    'name': 'Celeb 2',
                    'worth': '23000000'
                },
                {
                    'name': 'Celeb 3',
                    'worth': '1000007'
                },
                {
                    'name': 'Celeb 4',
                    'worth': '456789'
                },
                {
                    'name': 'Celeb 5',
                    'worth': '7890000'
                },
                {
                    'name': 'Celeb 6',
                    'worth': '12000456'
                },
                {
                    'name': 'Celeb 7',
                    'worth': '896000'
                },
                {
                    'name': 'Celeb 8',
                    'worth': '670000'
                }
            ]
        }

        return render(request, 'data.html', context)
