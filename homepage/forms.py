from django import forms
from .models import UserUploads

class UserForm(forms.ModelForm):
    class Meta:
        model = UserUploads
        fields = "__all__"

class getDetails(forms.Form):
    data_input = forms.CharField(max_length=225)