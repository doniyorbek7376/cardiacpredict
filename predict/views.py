from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import PredictionModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # replace 'home' with the name of your homepage url
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("redirecting")
            return redirect('home')  # replace 'home' with the name of your homepage url
        return render(request, 'login.html', context={"error": "Invalid username or password"})
    return render(request, 'login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect("login/")
    print(request.user)
    form = UserInputForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_data = [
                1 if form.cleaned_data['sex'] == 'Male' else 0,
                form.cleaned_data['age'],
                form.cleaned_data['cigs_per_day'] > 0,
                form.cleaned_data['cigs_per_day'],
                form.cleaned_data['bp_meds'],
                form.cleaned_data['prevalent_stroke'],
                form.cleaned_data['prevalent_hyp'],
                form.cleaned_data['diabetes'],
                form.cleaned_data['tot_chol'],
                form.cleaned_data['sys_bp'],
                form.cleaned_data['dia_bp'],
                form.cleaned_data['weight'] / (form.cleaned_data['height']/100)**2,
                form.cleaned_data['heart_rate'],
                form.cleaned_data['glucose']
            ]

            prediction_model = PredictionModel.objects.get(name='framingham')
            result = prediction_model.predict([user_data])
            context['prediction'] = result[0] * 100
            form = UserInputForm(request.POST)
            context['form'] = form
    return render(request, 'home.html', context)

