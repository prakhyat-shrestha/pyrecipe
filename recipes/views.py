from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RecipeForm
from .models import Recipe

def recipe_create(request):
	form = RecipeForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Hurray!! Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	"form" : form
	}
	return render(request, "recipe_form.html",context)

def recipe_detail(request, id):
	instance = get_object_or_404(Recipe, id=id)
	context = {
		"title" : instance.recipeName,
		"instance": instance
	}
	return render(request, "recipe_detail.html", context)
	
def recipe_list(request):
	queryset = Recipe.objects.all()

	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(recipeName__icontains=query) |
			Q(recipeInstructions__icontains=query) |
			Q(recipeIngredients__icontains=query) 
			).distinct()
	context = {
		"object_list": queryset,
		"title": " Recipe List"
	}
	return render(request, "recipe_list.html", context)
	
def recipe_update(request, id=None):
	instance = get_object_or_404(Recipe, id=id)
	form = RecipeForm(request.POST or None,instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Hurray!! Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title" : instance.recipeName,
		"instance": instance,
		"form" : form
	}
	return render(request, "recipe_form.html", context)
	
def recipe_delete(request,id = None):
	instance = get_object_or_404(Recipe, id=id)
	instance.delete()
	messages.success(request, "Item Deleted")
	return redirect("list")
