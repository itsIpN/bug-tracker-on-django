 
from django import forms
from .models import Project, Bugs

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class BugForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('title', 'comments', 'status', 'priority', 'fixed', 'project')
        widgets = {
            'project': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Title'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'fixed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    def __init__(self, *args, **kwargs):
        if 'project' in kwargs:
            project = kwargs.pop('project')
            kwargs.update(initial={
                'project': project
            })
        super(BugForm, self).__init__(**kwargs)
        self.fields['project'].label = ""


class BugUpdateForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('comments', 'status', 'priority', 'fixed')
        widgets = {
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'fixed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }