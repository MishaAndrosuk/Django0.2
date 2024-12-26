from django import forms
from films.models import Film
from datetime import date

class EditFiml(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"