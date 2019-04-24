from django import forms

from .models import Modelos

class ModelsForm(forms.ModelForm):
    class Meta:
        model = Modelos
        fields = ('title', 'name', 'description', 'instructions', 'predictor','dataset')