from django import forms
from .models import article_model

class write_form(forms.ModelForm):
    class Meta:
        model = article_model
        fields = ('title','body')