# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
# Added by sumit
# Source: https://www.digitalocean.com/community/tutorials/how-to-create-django-models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):

# to give user defined table name
# source: https://coderwall.com/p/xaljjg/custom-table-name-in-django-model

# password field source: https://stackoverflow.com/questions/3715103/password-field-in-django-model
    class Meta:
        db_table = 'users'
    user_id = models.CharField(max_length=10)
    user_pass = models.CharField(('password'), max_length=10, help_text=("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
    full_name = models.CharField(max_length=30)
    def __str__(self):
        return self.user_id

class Ctxapacusers(models.Model):
#    class Meta:
#        db_table = 'apacusers'
    user_name = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=50)
    emp_contact = models.CharField(max_length=15)
    def __str__(self):
        return self.user_name

class Skills(models.Model):
    skills = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.skills

class Skills_map(models.Model):
    user_id = models.ForeignKey(Ctxapacusers, on_delete=models.CASCADE)
    skill_name = models.ForeignKey(Skills, on_delete=models.CASCADE)
    skill_level = models.IntegerField()
    def __str__(self):
        return self.skill_level




#    def set_password(self, raw_password):
#        import random
#        algo = 'sha1'
#        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
#        hsh = get_hexdigest(algo, salt, raw_password)
#        self.user_pass = '%s$%s$%s' % (algo, salt, hsh)

#        return '%s (%s)' % (self.user_id,self.full_name)
#class Employee(models.Model):
#    """docstring fo:q:q!r Employee.models.Modelef __init__(self, arg):
#        super(Employee,models.Model.__init__()
#        self.arg = arg
