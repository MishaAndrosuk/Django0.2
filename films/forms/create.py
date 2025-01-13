from django import forms
from films.models import Film
import datetime

class CreateFilm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets = {
            'genre': forms.Select(attrs={'class': 'form-select'}),
        }


    def clean_year(self):
        year = self.cleaned_data.get("year")
        current_year = datetime.datetime.now().year
        if year > current_year:
            raise forms.ValidationError("Year cannot be greater than the current year.")
        return year

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating < 0 or rating > 10:
            raise forms.ValidationError("The rating must be between 0 and 10.")
        return rating

    def clean_runtime(self):
        runtime = self.cleaned_data.get("runtime")
        if runtime <= 0:
            raise forms.ValidationError("Runtime must be a positive number.")
        return runtime

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise forms.ValidationError("The title must be at least 2 characters long.")
        return title
    

    def clean_director(self):
        director = self.cleaned_data.get("director")
        if len(director) < 2:
            raise forms.ValidationError("The director's name must be at least 2 characters long.")
        return director
    


