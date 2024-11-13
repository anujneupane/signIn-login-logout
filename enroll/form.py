from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class Sign(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',]
        labels = {}

class Changeuser(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email': 'Email'} 