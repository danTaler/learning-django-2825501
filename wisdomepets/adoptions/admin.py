from django.contrib import admin

# Register your models here.
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    #pass
    # mispelled - breed
    list_display = ['name','species','bread', 'age', 'sex']

