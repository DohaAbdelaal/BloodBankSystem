from django import forms
from django.core.validators import MinLengthValidator
from .models import donor

class DonorForm(forms.ModelForm):
    National_ID = forms.CharField(max_length=14, validators=[MinLengthValidator(14)],
                                  label='National ID')
    Name = forms.CharField(max_length=50)
    City = forms.CharField(max_length=20)
    Email = forms.EmailField(max_length=254)
    virus_test = forms.ChoiceField(choices=[('negative', 'Negative'), ('positive', 'Positive')],
                                   widget=forms.RadioSelect, label='Virus Test')
    last_donation_3_months = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')],
                                               widget=forms.RadioSelect,
                                               label='Did you spend 3 months since your last donation?')

    class Meta:
        model = donor
        fields = ['National_ID', 'Name', 'City', 'Email']

    def save(self, commit=True):
        # Since 'virus_test' and 'last_donation_3_months' are not model fields, we handle their data separately
        if commit:
            instance = super(DonorForm, self).save(commit=False)
            instance.virus_test = self.cleaned_data['virus_test']
            instance.last_donation_3_months = self.cleaned_data['last_donation_3_months']
            instance.save()
        return instance
