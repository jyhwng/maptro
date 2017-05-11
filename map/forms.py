from django import forms
from .models import Nick

class NickForm(forms.ModelForm):
    class Meta:
        model = Nick
        # exclude = (
        #     'like',
        # )
        fields = (
            'name',
        )
        widgets = {
            'name' : forms.Textarea(attrs = {'class' : 'form-control', 'rows' : 1}),
        }
