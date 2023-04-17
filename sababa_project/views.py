from django.http import HttpResponse
from django.shortcuts import render


def template_test(request):
    return render(request, "hello_world.html")


def home_page(request):
    return HttpResponse("<h1>Hello!</h1>")
