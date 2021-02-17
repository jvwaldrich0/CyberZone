from django import forms
from .models import post

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('background', 'title', 'summary', 'content', 'author')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:#363636;'}),
            'summary' : forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:#363636;'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color:black; color:grey;border-color:#363636;'}), 
            'author' : forms.TextInput(attrs={'class': 'form-control',
                                              'value':'',
                                              'id':'elder',
                                              'type':'hidden'}),
            }