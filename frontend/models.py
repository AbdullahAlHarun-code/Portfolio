from django.db import models
from django.contrib import admin
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ManyToManyField('Category', related_name='subCategories')
    def __str__(self):
        c_name_list= "\n | ".join([p.name for p in self.parent_category.all()])
        return self.name+' | ('+c_name_list+')'
    
    

# class SubCategory(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey("Category", on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
# class TestBlock(models.Model):
#     title = models.CharField(max_length=200)
#     sub_category = models.ManyToManyField('Test2Category', related_name='blocks')

#     def __str__(self):
#         return self.title

class Block(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='block/images/', blank=True, null=True)
    link = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
    sub_category = models.ManyToManyField("SubCategory", related_name=("blocks"))

    def __str__(self):
        return self.title

    