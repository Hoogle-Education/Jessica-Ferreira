from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_all(request):
  return render("user/index.html")

def register(request):
  return HttpResponse("Register")