from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sigma
from sigma_stone import settings
import os

# Create your views here.
def list(request):
    return render(request, "list.html", {"sigmas":Sigma.objects.all(), "count":Sigma.objects.all().count()})

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        description = request.POST.get("description")
        photo = request.FILES['photo']
        sigma = Sigma(name=name, city=city, description=description, photo=photo)
        sigma.save()
        return redirect("/personalities/list")

def delete(request, id):
    sigma = get_object_or_404(Sigma, id=id)
    os.remove(f'{settings.BASE_DIR}/media/{sigma.photo}')
    sigma.delete()
    return redirect('/personalities/list')
