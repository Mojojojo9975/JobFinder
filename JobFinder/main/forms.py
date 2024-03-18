
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms.models import ModelForm
from django.forms.widgets import FileInput


        

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profileImage']
        widgets={'profileImage':FileInput(attrs={"class":"form-control"}) }
