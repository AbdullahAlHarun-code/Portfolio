from .models import (
    Category, 
    SubCategory, 
    Block)
class Portfolio:
    def __init__(self):
        self.title = ''

class About:

    def __init__(self):
        self.title = ''
        self.sub_title = ''
        self.image = ''
        self.another_intro_title = ''
        self.another_intro_sub_title = ''
        self.another_para = ''
        self.frontend_backend = ''
        self.generateValue()
    def generateValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='about').order_by('hierarchy')
        self.title = blocks.filter(sub_category__name='intro').first().title
        self.sub_title = blocks.filter(sub_category__name='intro').first().text
        self.image = blocks.filter(sub_category__name='image').first().image

        self.another_intro_title = blocks.filter(sub_category__name='another intro').first().title
        self.another_intro_sub_title = blocks.filter(sub_category__name='another intro').first().text
        self.another_para = blocks.filter(sub_category__name='another intro').first().description

        self.frontend_backend = blocks.filter(sub_category__name='frontend and backend').first().text


class DefaultInfo:

    def __init__(self):
        self.title = ''
        self.logo = ''
        self.favicon = ''
        self.generateValue()
    def generateValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='default info').order_by('hierarchy')
        self.title = blocks.filter(sub_category__name='logo').first().title
        self.logo = blocks.filter(sub_category__name='logo').first().image
        self.favicon = blocks.filter(sub_category__name='favicon').first().image

class PersonalInfo:

    def __init__(self):
        self.name = ''
        self.phone = ''
        self.email = ''
        self.facebook = ''
        self.twtitter = ''
        self.generateValue()
    def generateValue(self):
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
        self.generateValue()
    def generateValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='section 1').order_by('hierarchy')
        self.title = blocks.filter(sub_category__name='section 1 title and subtitle').first().title
        self.para = blocks.filter(sub_category__name='section 1 title and subtitle').first().text
        self.image = blocks.filter(sub_category__name='section 1 title and subtitle').first().image


class Services:

    def __init__(self):
        self.card = {}
        self.title = ''
        self.sub_title = ''
        self.footer_text = ''
        self.generateValue()
    def generateValue(self):
        blocks = Block.objects.filter(active=True, sub_category__parent_category__name='services').order_by('hierarchy')
        self.card = blocks.filter(sub_category__name='services section card')
        self.title = blocks.filter(sub_category__name='services text').first().title
        self.sub_title = blocks.filter(sub_category__name='services text').first().text
        self.footer_text = blocks.filter(sub_category__name='services text').first().description