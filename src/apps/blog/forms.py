from django import forms
from .models import post

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('background', 'title', 'summary', 'content', 'author')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:green;'}),
            'summary' : forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:green;'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:green;'}), 
            'author' : forms.TextInput(attrs={'class': 'form-control',
                                              'value':'',
                                              'id':'elder',
                                              'type':'hidden'}),
            }