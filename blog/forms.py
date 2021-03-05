from django import forms
from .models import Temoignage

class TemoignagesForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = 'titre','pseudo','resume','contenu'

