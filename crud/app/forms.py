from django import forms
from app.models import Details

class Detailsform(forms.ModelForm):
    class Meta:
        model=Details
        fields="__all__"
        
    
    
