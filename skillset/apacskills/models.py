# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#class Employees(models.Model):

# to give user defined table name
# source: https://coderwall.com/p/xaljjg/custom-table-name-in-django-model

# password field source: https://stackoverflow.com/questions/3715103/password-field-in-django-model
#    class Meta:
#        db_table = 'users'
#    user_id = models.CharField(max_length=10)
#    user_pass = models.CharField(('password'), max_length=10, help_text=("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
#    full_name = models.CharField(max_length=30)
#    def __str__(self):
#        return self.user_id

class Ctxapacusers(models.Model):
#    class Meta:
#        db_table = 'apacusers'
    user_name = models.CharField(primary_key=True, unique=True, max_length=10)
    full_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=50)
    emp_contact = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user_name

class Skills(models.Model):
    skills = models.CharField(primary_key=True, max_length=50, unique=True)
    def __str__(self):
        return self.skills

class Skills_map(models.Model):
    user_id = models.ForeignKey(Ctxapacusers, on_delete=models.CASCADE)
    skill_name = models.ForeignKey(Skills, on_delete=models.CASCADE)
    #skill_level = models.IntegerField()
    skill_level = models.CharField(max_length=1, choices=(('S', 'SME'),('Y', 'Support')))
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.skill_level
