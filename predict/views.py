from django.shortcuts import render
from .forms import UserInputForm
from .models import PredictionModel

def home(request):
    form = UserInputForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_data = [
                1 if form.cleaned_data['sex'] == 'Male' else 0,
                form.cleaned_data['age'],
                form.cleaned_data['current_smoker'],
                form.cleaned_data['cigs_per_day'],
                form.cleaned_data['bp_meds'],
                form.cleaned_data['prevalent_stroke'],
                form.cleaned_data['prevalent_hyp'],
                form.cleaned_data['diabetes'],
                form.cleaned_data['tot_chol'],
                form.cleaned_data['sys_bp'],
                form.cleaned_data['dia_bp'],
                form.cleaned_data['bmi'],
                form.cleaned_data['heart_rate'],
                form.cleaned_data['glucose']
            ]

            prediction_model = PredictionModel.objects.get(name='framingham')
            result = prediction_model.predict([user_data])
            context['prediction'] = result[0] * 100
    return render(request, 'home.html', context)

