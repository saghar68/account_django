from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import Customuser
# Register your models here.


class UserCustomAdmin(UserAdmin):
    add_form=UserCreateForm
    form=UserChangeForm
    model=Customuser
    fieldsets=UserAdmin.fieldsets+(
        (None,{'fields':('age',)}),
    )
    add_fieldsets=UserAdmin.fieldsets+(
        (None,{'fields':('age',)}),
    )
    #list_display=['username','age']
    
admin.site.register(Customuser,UserCustomAdmin)