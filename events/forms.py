from django import forms
from django.forms import ModelForm
from .models import information
import time
 
#https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets
# Create a information forma
class InformationForm(ModelForm):
    class Meta: 
        model = information
        fields = ('name', 
        #'interest', 
        'introduction', 
        'recent_events',  
        'autobiography',
        'refresh_date',
        'image', 
        )
        
        #自訂label
        labels = {
            'name': '',#'Enter your name',
            #'interest': '',#'"Your interest" No more say',
            'introduction': '',#'Introduction yourself',
            'recent_events': '',#'Describe what interesting thing happened recently',
            'refresh_date': 'lastest action date ',
            'autobiography': '',#'Describe your life-time',            
            'image': '',
        } 
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name : Enter your name'}),
            #'interest': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Interest : No more say playlol'}),
            'introduction': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduction : Introduce yourself roughly'}),
            'recent_events': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recent_events : Describe what interesting thing happened recently'}),
            #'refresh_date': forms.DateInput(attrs={'type':'date', 'class':'form-control', 'placeholder':'Refresh_date : lastest action date'}),
            'autobiography': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Autobiography : Describe your life-time'}),      
        }
