from django import forms
from django.forms import ModelForm
from .models import paper
import time
 

# Create a information forma
class paperForm(ModelForm):
    class Meta: 
        model = paper
        fields = ('papername', 
        'papercontent', 
        'image',  
        )
        
        #自訂label
        labels = {
            'papername': '',#'Enter your papername',
            'papercontent': '',#'papercontent',
            'image': '',#'image',
        } 
        
        widgets = {
            'papername': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Papername : Enter your papername'}),         
            'papercontent': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content '}),
        }
