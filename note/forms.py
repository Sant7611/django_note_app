from django import forms
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'description', 'image']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Note title here...',
                    'class': 'w-full px-2 py-2 bg-gray-100 border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 mb-4'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Note details here...',
                    'rows': 2,
                    'class': 'w-full px-2 py-2 bg-gray-100 border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none'
                }
            )
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with email already exists...")
        return email
