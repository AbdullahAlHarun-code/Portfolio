from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Category, 
    SubCategory, 
    Block)

# Create your views here.

def home(request):
    template_name = 'frontend/home.html'
    categories = Category.objects.all().filter(name='services')
    blocks = Block.objects.filter(blocks='service section card')
    #categories = Category.objects.sub_category(1)
    # for block in blocks:
    #     print('Block',block)
    # for cat in categories:
    #     #print('cat anme',cat.name)
    #     for subcat in cat.subCategories.all():
    #         for block in subcat.blocks.all():
    #             print(block)
    context = {'category':categories}
    return render(request, template_name, context)
