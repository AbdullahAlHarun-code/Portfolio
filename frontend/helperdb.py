from .models import (
    Category, 
    SubCategory, 
    Block)

class DefaultInfo:

    def __init__(self):
        self.logo = ''
        self.generatValue()
    def generatValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='default info').order_by('hierarchy')
        self.logo = blocks.filter(sub_category__name='logo').first().image

class PersonalInfo:

    def __init__(self):
        self.name = ''
        self.phone = ''
        self.email = ''
        self.facebook = ''
        self.twtitter = ''
        self.generatValue()
    def generatValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='personal info').order_by('hierarchy')
        self.name = blocks.filter(sub_category__name='name').first().title
        self.email = blocks.filter(sub_category__name='email').first().title
        self.phone = blocks.filter(sub_category__name='phone number').first().title

class SectionOne:

    def __init__(self):
        self.title = ''
        self.subtile = ''
        self.para = ''
        self.button_text = ''
        self.button_link = ''
        self.image = ''
        self.generatValue()
    def generatValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='section 1').order_by('hierarchy')
        self.title = blocks.filter(sub_category__name='section 1 title and subtitle').first().title
        self.para = blocks.filter(sub_category__name='section 1 title and subtitle').first().text
        self.image = blocks.filter(sub_category__name='section 1 title and subtitle').first().image


