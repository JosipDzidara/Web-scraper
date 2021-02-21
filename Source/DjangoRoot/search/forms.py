from django import forms

class MachineLearningForm(forms.Form):
    county = forms.ChoiceField(choices=(('Bjelovarsko-bilogorska','Bjelovarsko-bilogorska'),('Brodsko-posavska','Brodsko-posavska')))
    n_room = forms.IntegerField(label='Number of rooms')
    sqr_out = forms.IntegerField(label='Outer area')
    sqr_in = forms.IntegerField(label='Inner area')
    see_view = forms.ChoiceField(choices=[(1 ,'Da'),(0 ,'Ne')])

