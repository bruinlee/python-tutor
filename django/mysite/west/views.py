from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from west.models import Character

def first_page(request):
    return HttpResponse("<p>west</p>")

def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    return HttpResponse("<p>" + " ".join(staff_str) + "</p>")
