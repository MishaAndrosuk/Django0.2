from django import forms
from users.models import User
from datetime import date

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Цей email уже використовується іншим користувачем.")
        return email

    def clean_birthday(self):
        birthday = self.cleaned_data.get("birthday")
        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        
        if age < 18:
            raise forms.ValidationError("Користувач повинен бути старше 18 років.")
        return birthday

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if not first_name or not last_name:
            raise forms.ValidationError("Ім'я та прізвище обов’язкові для заповнення.")
        return cleaned_data
