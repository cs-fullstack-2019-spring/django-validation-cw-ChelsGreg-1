from django import forms
from .models import CarModel

# FORM TO INPUT MODEL DETAILS
class CarForm(forms.ModelForm):
    class Meta:
        model= CarModel
        fields = "__all__"


# FOR MILE VALIDATIONS
    def clean_mpg(self):
        miles = self.cleaned_data["mpg"]

        if miles < 20:
            raise forms.ValidationError("That's less than a truck!!!")
        if miles > 500:
            raise forms.ValidationError("That's impossible..currently!")

        return miles

# FOR YEAR VALIDATION
    def clean_year(self):
        newYear = self.cleaned_data["year"]

        if newYear < 2019:
            raise forms.ValidationError("That's not new!")

        return newYear