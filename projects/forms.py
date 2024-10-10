from django import forms
from . import models
from django.utils.translation import gettext as _


atters = {'class' : 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        labels = {
            'category' : _('Category'),
            'title' : _('Title'),
            'description' : _('Description')
        }
        widgets = {
            'category': forms.Select( attrs=atters),
            'title': forms.TextInput(attrs=atters),
            'description': forms.Textarea(attrs=atters)
        }

class ProjectUdateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs=atters),
            'title': forms.TextInput(attrs=atters),
            'status': forms.Select(attrs=atters)
        }


