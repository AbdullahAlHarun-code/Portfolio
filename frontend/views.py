from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Category, 
    SubCategory, 
    Block)
from .serializers import BlockSerializers
from .helperdb import (
    PersonalInfo,
    SectionOne,
    DefaultInfo,
    About,
    Services,
    )
# Create your views here.

def home(request):
    template_name = 'frontend/home.html'
    categories = Category.objects.all().filter(name='services')
    # sub_category_blocks = SubCategory.objects.filter(blocks__in=[2])
    # for block in sub_category_blocks:
    #     print('Block',block)
    all_blocks = Block.objects.filter(active=True).order_by('hierarchy')
    blocks = Block.objects.filter(active=True, sub_category__parent_category__name='services').order_by('hierarchy')
    services_card = blocks.filter(sub_category__name='service section card')
    resume_education = all_blocks.filter(sub_category__parent_category__name='resume', sub_category__name='education')
    resume_experience = all_blocks.filter(sub_category__parent_category__name='resume', sub_category__name='experience')
    personal_info = PersonalInfo()
    section_one = SectionOne()
    default_info =DefaultInfo()
    about = About()
    services =Services()
    context = {
        'category':categories,
        'services_card':services_card,
        'personal_info': personal_info,
        'section_one': SectionOne,
        'default_info': default_info,
        'about': about,
        'services':services,
        'resume_education': resume_education,
        'resume_experience': resume_experience,
        }
    return render(request, template_name, context)
