from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    ingredients = models.CharField(max_length=200)
    process = models.TextField()
    recipe_img = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name

    # def get_recipe_img(self):
    #     if self.recipe_img:
    #         return self.recipe_img.url
    #     else:
    #         return "/media/images/1.jpg"

