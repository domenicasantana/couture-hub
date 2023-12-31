from django import forms
from django.forms import TextInput, FileInput, Select, Textarea
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'slug',
            'thumb',
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control mx-auto",
                'placeholder': 'Title'
                }),
            'body': Textarea(attrs={
                'class': "form-control mx-auto",
                'placeholder': 'Your awesome article here'
                }),
            'slug': TextInput(attrs={
                'class': "form-control mx-auto",
                'placeholder': 'Slug'
                }),
            'thumb': FileInput(attrs={
                'class': "form-control mx-auto custom-thumb-input", 
                'style': 'max-width: 300px;',
                }),

        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'slug',
            'thumb',
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control mx-auto",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'body': Textarea(attrs={
                'class': "form-control mx-auto",
                'style': 'max-width: 800px;',
                'placeholder': 'Your awesome article here'
                }),
            'slug': TextInput(attrs={
                'class': "form-control mx-auto",
                'style': 'max-width: 300px;',
                'placeholder': 'Slug'
                }),
            'thumb': FileInput(attrs={
                'class': "form-control mx-auto", 
                'style': 'max-width: 300px;',
                }),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            'content'
        ]
        widgets = {
            'content': Textarea(attrs={
                'class': "form-control mx-auto",
                'style': 'max-width: 800px;',
                'placeholder': 'Your awesome comment here'
                }),
        }