from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class Index ():
    def setup (request):
        something = "your looking at the home page"
        context = {'response' : something}
        return render(request, 'home/index.html', context)
