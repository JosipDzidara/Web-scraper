from django import forms

class NameForm(forms.Form):
    page = forms.CharField(label='Sumbit a search')