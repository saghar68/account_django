from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import Customuser




class UserCreateForm(UserCreationForm):
    class Meta:
        model=Customuser
        #fields=UserCreationForm.Meta.fields+('age',)
        fields=('username','age','email')
        
class UserChangeForm(UserChangeForm):
    class Meta:
        model=Customuser
        #fields=UserChangeForm.Meta.fields
        fields=('username','age','email')   