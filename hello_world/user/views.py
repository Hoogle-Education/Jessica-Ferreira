from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_all(request):
  return HttpResponse("Get All")

def register(request):
  return HttpResponse("Register")