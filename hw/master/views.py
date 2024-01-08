from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def members(request):
    return HttpResponse("Hello world!")


def sample(request):
  template = loader.get_template('sample.html')
  return HttpResponse(template.render())


from .models import Member

def allmembers(request):
  mymembers = Member.objects.all().values()
  print(mymembers)
  template = loader.get_template('all_mem.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))    