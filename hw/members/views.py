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
  template = loader.get_template('all_members.html')
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