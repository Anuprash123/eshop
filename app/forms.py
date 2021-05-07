from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
