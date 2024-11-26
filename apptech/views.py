from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def display_home(request):
    name = request.GET["txtname"]
    password = request.GET["txtpassword"]
    return HttpResponse(f"<h1> my name is {name} <br> " f" my password is {password} <br> </h1>")
