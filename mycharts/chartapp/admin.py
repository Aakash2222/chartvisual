from django.contrib import admin
from .models import Product
from .models import Signup

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'topic','title'
    )


# admin.site.register(Product)

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('username','email')

# admin.site.register(Signup)


