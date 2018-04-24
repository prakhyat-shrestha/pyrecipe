from django.contrib import admin

# Register your models here.

from .models import Recipe

class RecipeModelAdmin(admin.ModelAdmin):
	list_display = ["recipeName","timestamp"]
	list_filter = ["timestamp"]
	search_fields = ["recipeName","recipeIngredients"]
	class Meta:
		model = Recipe

admin.site.register(Recipe, RecipeModelAdmin)