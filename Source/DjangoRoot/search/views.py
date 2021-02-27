
from django.shortcuts import render
from ML_Model.ml_model import MachineLearningModel
from .forms import MachineLearningForm


def calculate_result(request):
    if request.method == "POST":
        form = MachineLearningForm(request.POST)
        if form.is_valid():
            county = form.cleaned_data['county']
            n_room = form.cleaned_data['n_room']
            sqr_out = form.cleaned_data['sqr_out']
            sqr_in = form.cleaned_data['sqr_in']
            sea_view = form.cleaned_data['sea_view']
            result = [n_room, sqr_out, sqr_in, int(sea_view), county]
            model = MachineLearningModel('OLS', result)
            prediction = model.start_ml_analysis()
            result.append(prediction)
            return render(request, 'search/result.html', {'result': result})

    form = MachineLearningForm()
    return render(request, 'search/index.html', {'form': form})
