from django.forms import ModelForm
from django import forms
from .models import User, News, Comment

class Register(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content', 'active')

class NewsComment(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'comment something...'
        }),
        required=True)

    class Meta():
        model = Comment
        fields = ['comment', '']

