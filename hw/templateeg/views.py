from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

def variables(request):
  template = loader.get_template('variable.html')
  context = {
    'firstname': 'Vishwa',
  }
  return HttpResponse(template.render(context, request))


def varintemplate(request):
  template = loader.get_template('varintemplate.html')
  return HttpResponse(template.render())


def listtest(request):
  template = loader.get_template('list.html')
  context = {
    'mymembers': [{"firstname":"Rajeev"},{"firstname":"Vishwa"}],
  }
  return HttpResponse(template.render(context, request))


def ifelseeg(request):
  template = loader.get_template('ifelseeg.html')
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return HttpResponse(template.render(context, request))  

def fornested(request):
  template = loader.get_template('fornested.html')
  context = {
      "emptytestobject":[{}],
   'members':[
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes',
    'phone': 5551234,
    'joined_date': datetime.date(2022, 1, 5)
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes',
    'phone': 5557777,
    'joined_date': datetime.date(2021, 4, 1)
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes',
    'phone': 5554321,
    'joined_date': datetime.date(2021, 12, 24)
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes',
    'phone': 5551234,
    'joined_date': datetime.date(2021, 5, 1)
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes',
    'phone': 5559876,
    'joined_date': datetime.date(2022, 9, 29)
  }
]
  }
  return HttpResponse(template.render(context, request))  

