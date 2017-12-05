# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from apacskills.models import Ctxapacusers, Skills, Skills_map
from django.contrib.auth.forms import UserCreationFormakes no parameters
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.detail import SingleObjectMixin
from django.views import View


class Sumitview:
    """docstring for ."""
    def __init__(self):
        return "created";
    def Helloworld():
        return "Hwlloworld"
