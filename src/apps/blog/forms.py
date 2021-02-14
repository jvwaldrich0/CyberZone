from django import forms
from .models import post

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('background', 'title', 'summary', 'content', 'author')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'summary' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}), 
            'author' : forms.TextInput(attrs={'class': 'form-control',
                                              'value':'',
                                              'id':'elder',
                                              'type':'hidden'}),
            }