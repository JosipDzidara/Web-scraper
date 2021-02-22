from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.bootstrap import FormActions


counties_list = ['Bjelovarsko-bilogorska', 'Brodsko-posavska', 'Dubrovačko-neretvanska',
                 'Grad Zagreb', 'Istarska', 'Karlovačka', 'Koprivničko-križevačka',
                 'Krapinsko-zagorska', 'Ličko-senjska', 'Međimurska',
                 'Osječko-baranjska', 'Požeško-slavonska', 'Primorsko-goranska',
                 'Sisačko-moslavačka', 'Splitsko-dalmatinska', 'Varaždinska',
                 'Virovitičko-podravska', 'Vukovarsko-srijemska', 'Zadarska',
                 'Zagrebačka', 'Šibensko-kninska']
county_choices = set()
for county in counties_list:
    county_choices.add((county, county))


class MachineLearningForm(forms.Form):
    county = forms.ChoiceField(choices=county_choices, widget=forms.Select)
    n_room = forms.IntegerField(label='Number of rooms')
    sqr_out = forms.IntegerField(label='Outer area')
    sqr_in = forms.IntegerField(label='Inner area')
    sea_view = forms.ChoiceField(choices=((1, 'Da'), (0, 'Ne')), widget=forms.RadioSelect)

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        'county',
        Field('n_room', style="background: #FAFAFA; padding: 10px;"),
        Field('sqr_out', style="background: #FAFAFA; padding: 10px;"),
        Field('sqr_in', style="background: #FAFAFA; padding: 10px;"),
        'sea_view'
    )
