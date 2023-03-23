from django import forms
from .models import Player, Season

class PlayerForm(forms.ModelForm):
    season = forms.ModelChoiceField(queryset=Season.objects.all())

    class Meta:
        model = Player
        exclude = ('user',)


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = '__all__'
