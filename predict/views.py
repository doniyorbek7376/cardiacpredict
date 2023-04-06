from django.shortcuts import render
from .forms import UserInputForm
from .models import PredictionModel

def home(request):
    form = UserInputForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_data = {
                'male': 1 if form.cleaned_data['sex'] == 'Male' else 0,
                'age': form.cleaned_data['age'],
                'currentSmoker': form.cleaned_data['current_smoker'],
                'cigsPerDay': form.cleaned_data['cigs_per_day'],
                'BPMeds': form.cleaned_data['bp_meds'],
                'prevalentStroke': form.cleaned_data['prevalent_stroke'],
                'prevalentHyp': form.cleaned_data['prevalent_hyp'],
                'diabetes': form.cleaned_data['diabetes'],
                'totChol': form.cleaned_data['tot_chol'],
                'sysBP': form.cleaned_data['sys_bp'],
                'diaBP': form.cleaned_data['dia_bp'],
                'BMI': form.cleaned_data['bmi'],
                'heartRate': form.cleaned_data['heart_rate'],
                'glucose': form.cleaned_data['glucose']
            }

            prediction_model = PredictionModel.objects.get(name='framingham')
            result = prediction_model.predict([[value for value in user_data.values()]])
            context['prediction'] = result
    return render(request, 'home.html', context)

