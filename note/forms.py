from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'description']

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