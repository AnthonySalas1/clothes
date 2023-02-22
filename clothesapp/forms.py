from .models import *
from django import forms

class itemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
