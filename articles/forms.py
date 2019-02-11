from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.http import request


class CommentForm(forms.Form):

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea)
