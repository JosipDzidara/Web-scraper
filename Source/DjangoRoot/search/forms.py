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
ml_choices = ["Simple linear regression","Ridge Regression","Lasso Regression","Bayesian learning"]


county_choices = set()
for county in counties_list:
    county_choices.add((county, county))


class MachineLearningForm(forms.Form):
    model = forms.ChoiceField(choices=(('OLS', ml_choices[0]), ('Ridge', ml_choices[1]), ('Lasso', ml_choices[2]), ('Bayesian', ml_choices[-1])), widget=forms.Select)
    county = forms.ChoiceField(choices=county_choices, widget=forms.Select)
    n_room = forms.IntegerField(label='Number of rooms', min_value=1)
    sqr_out = forms.IntegerField(label='Outer area', min_value=1)
    sqr_in = forms.IntegerField(label='Inner area', min_value=1)
    sea_view = forms.ChoiceField(choices=((1, 'Yes'), (0, 'No')), widget=forms.RadioSelect)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Fieldset(
            'model',
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

