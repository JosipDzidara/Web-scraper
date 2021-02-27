from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, ButtonHolder, Fieldset
from django.core.validators import MinValueValidator

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
    n_room = forms.IntegerField(label='Number of rooms', validators=[MinValueValidator(1, message='Minimum number of '
                                                                                                  'rooms is 1.')])
    sqr_out = forms.IntegerField(label='Outer area', validators=[MinValueValidator(1, message='Minimum size of '
                                                                                                  'outer area is 1.')])
    sqr_in = forms.IntegerField(label='Inner area', validators=[MinValueValidator(1, message='Minimum size of '
                                                                                                  'iner area is 1.')])
    sea_view = forms.ChoiceField(choices=((1, 'Yes'), (0, 'No')), widget=forms.RadioSelect)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Fieldset(
            'county',
            Field('n_room', style="background: #FAFAFA; padding: 10px;"),
            Field('sqr_out', style="background: #FAFAFA; padding: 10px;"),
            Field('sqr_in', style="background: #FAFAFA; padding: 10px;"),
            'sea_view'
        ),
        ButtonHolder(
            Submit('submit', 'Submit', css_class='button white')
        )
    )

