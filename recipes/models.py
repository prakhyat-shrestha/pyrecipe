from django.db import models



# Create your models here.

class Recipe(models.Model):
	recipeName = models.CharField(max_length=240)
	recipeIngredients = models.TextField() 
	recipeInstructions = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


	def __str__(self):
		return self.recipeName

	def get_absolute_url(self):
	
		return "/recipes/%s/" %(self.id)

	def get_edit_url(self):
		return "/recipes/%s/edit" %(self.id)

	def get_delete_url(self):
		return "/recipes/%s/delete" %(self.id)
