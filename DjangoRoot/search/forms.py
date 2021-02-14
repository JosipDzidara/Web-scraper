from django import forms

class ml_input(forms.Form):
    county = forms.ChoiceField(choices=[('c1','SB'),('c2','ZG')])
    n_room = forms.IntegerField(label='Number of rooms')
    sqr_out = forms.IntegerField(label='Outer area')
    sqr_in = forms.IntegerField(label='Inner area')
    see_view = forms.ChoiceField(choices=[(1 ,'Da'),(0 ,'Ne')])

