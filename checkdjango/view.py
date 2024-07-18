from django.http import HttpResponse
from django.views import *

def showing (self,request, *args, **kwargs):
      return HttpResponse("Hello, this is the show view. The arguments are: " + str(args) + " and " + str(kwargs))