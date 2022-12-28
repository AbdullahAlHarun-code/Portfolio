from django.contrib import admin
from .models import (Category, SubCategory, Block)
# Register your models here.

# class SubCategoryAdmin(admin.TabularInline):
#     model = SubCategory
#     extra = 0



#     def get_sub_category(self, obj):
#         return "\n | ".join([p.name for p in obj.sub_category.all()])

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','get_parent_category']
    list_filter = ['parent_category'] 
    filter_horizontal = ('parent_category',)

    def get_parent_category(self, obj):
        return "\n | ".join([p.name for p in obj.parent_category.all()])

class BlockAdmin(admin.ModelAdmin):
    list_display = ['title','get_sub_category', 'get_parent_category']
    list_filter = ['sub_category__parent_category',] 
    filter_horizontal = ('sub_category',)

    def get_sub_category(self, obj):
        return "\n | ".join([p.name for p in obj.sub_category.all()])
        
    def get_parent_sub_category(self, obj):
        return "\n | ".join([p.name for p in obj.sub_category.all()])
    
    def get_parent_category(self, obj):
        sub_categories = obj.sub_category.all()
        c_name_list = ''
        for pc in sub_categories:
            c_name_list= "\n | ".join([p.name for p in pc.parent_category.all()])
        return c_name_list

# class Test1CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     list_filter = ['parent_category'] 
#     filter_horizontal = ('parent_category',)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     #list_filter = ('name') 
#     #filter_horizontal = ('SubCategory',)
# class BlockAdmin(admin.ModelAdmin):
#     list_display = ['title']
# class TestCatdmin(admin.ModelAdmin):
#     list_display = ['name', 'parent_category']
#     list_filter = ['parent_category']
    #filter_horizontal = ['parent_category',]


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Block, BlockAdmin)
# admin.site.register(TestCategory, TestCatdmin)
# admin.site.register(Test1Category)
# admin.site.register(Test2Category, Test2CategoryAdmin)
# admin.site.register(TestBlock, TestBlockAdmin)