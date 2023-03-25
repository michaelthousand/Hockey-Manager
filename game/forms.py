from django import forms
from .models import Event

class NoteForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('user', 'event_type',)