from django.shortcuts import render, redirect
from django.http import HttpResponse

from Model import ml_model as ml
from .forms import ml_input


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ml_input(request.POST)
        if form.is_valid():
            county = form.cleaned_data['county']
            n_room = form.cleaned_data['n_room']
            sqr_out = form.cleaned_data['sqr_out']
            sqr_in = form.cleaned_data['sqr_in']
            see_view = form.cleaned_data['see_view']
            result = [n_room, sqr_out, sqr_in, see_view, county]
            ml_model = ml.MachineLearningModel('ols', result)
            prediction = ml_model.prediction
            return render(request, 'search/result.html', {'result': prediction})

    form = ml_input()
    return render(request, 'search/form.html', {'form': form})

