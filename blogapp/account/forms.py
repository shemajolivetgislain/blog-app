from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User=get_user_model()
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password2']

class RegForm(forms.Form):
    username=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    password=forms.CharField(widget=forms.PasswordInput, required=True)
    password2=forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self):
        User.objects.create()
    def is_valid(self) -> bool:
        try:
            User.objects.get(username=self.username)
            raise forms.ValidationError("This username is already taken")
        except User.DoesNotExist:
            pass
        try:
            User.objects.get(email=self.email)
            raise forms.ValidationError("This email is already taken")
        except User.DoesNotExist:
            pass
        if self.password != self.password2:
            raise forms.ValidationError("Password needs to be similar")
        return True