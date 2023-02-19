from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

    list_display = ["name",'slug']
    


    '''def get_form(self, request, obj = None, **kwargs):


        form = super().get_form(request, obj, **kwargs)
        
        is_superuser = request.user.is_superuser
        
        if not is_superuser:
            form.base_fields['name'].disabled = True
            form.base_fields['slug'].disabled = True
            

        return form'''

    def get_form(self, request, obj = None, **kwargs):

        form = super().get_form(request, obj = None, **kwargs)

        is_superuser = request.user.is_superuser
        #is_staff = request.user.is_staff    


        if not is_superuser:

            form.base_fields['name'].disabled = True
            form.base_fields['slug'].disabled = True


        return form

