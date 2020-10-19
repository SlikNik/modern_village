from django import forms
from django.forms import ModelForm
from .models import Post


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
