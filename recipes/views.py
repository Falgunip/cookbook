from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
# Create your views here.
from django.urls import reverse



@login_required(login_url='/users/')
def index(request):
    # print("index function")
    name_list = Recipe.objects.order_by('-created_date')
    # print(name_list)
    return render(request, 'recipes/index.html', {'name_list':name_list})

@login_required(login_url='/users/')
def detail(request,recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe':recipe})

@login_required(login_url='/users/')
def create(request):
    # recipe = Recipe(name=request.POST.get('name'), ingredients=request.POST.get('ingredients'),
    #                 process=request.POST.get('process'))
    # recipe.save()
    return render(request, 'recipes/create.html')
    # return HttpResponseRedirect('/recipes/create')
    # try:
    #     # recipe = Recipe(name=request.POST.get('name'),ingredients=request.POST.get('ingredients'),process=request.POST.get('process'))
    #     recipe = Recipe(name=request.POST.get('name',''),ingredients=request.POST.get('ingredients',''),process=request.POST.get('process',''))
    #     recipe.save()
    # except(KeyError,Recipe.DoesNotExist):
    #     return render(request,'recipes/create.html',{'error_message': "You didn't enter any value"})
    # # return render(request, 'recipes/create.html', {'recipe': recipe})
    # return HttpResponseRedirect('')


def save(request):
    print(request.POST)
    print(request.FILES)
    recipe = Recipe(name=request.POST.get('name'), ingredients=request.POST.get('ingredients'),
                    process=request.POST.get('process'),recipe_img=request.FILES['recipe_img'])
    recipe.save()
    return HttpResponseRedirect('/recipes')
