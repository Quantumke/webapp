from django.contrib import admin
from app.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={ 'slug':['title'] }

admin.site.register(Category, CategoryAdmin)

class ScalesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':['scale_name']}


admin.site.register(scales, ScalesAdmin)


