from accounts.models import Contact, Post
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name','last_name','email','content'
        ]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','image','body'
        ]

