from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import PredictionModel
from .serializers import RequestSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

import logging

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        logging.error(request.POST)
        logging.error(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user:User
                user.first_name = request.POST.get("first_name", user.first_name)
                user.last_name = request.POST.get("last_name", user.last_name)
                user.save()
                login(request, user)
                return redirect('home') 
        else:
            logging.error(form.errors)
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


def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.save()
        return redirect("home")
    return render(request, 'profile.html')

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

            prediction_model = PredictionModel.objects.filter(is_active=True).first()
            result = prediction_model.predict([user_data])
            context['prediction'] = result[0] * 100
            form = UserInputForm(request.POST)
            context['form'] = form
    return render(request, 'home.html', context)


class PredictAPI(APIView):
    def post(self, request: Request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            user_data = [
                1 if serializer.validated_data['sex'] == 'Male' else 0,
                serializer.validated_data['age'],
                serializer.validated_data['cigs_per_day'] > 0,
                serializer.validated_data['cigs_per_day'],
                serializer.validated_data['bp_meds'],
                serializer.validated_data['prevalent_stroke'],
                serializer.validated_data['prevalent_hyp'],
                serializer.validated_data['diabetes'],
                serializer.validated_data['tot_chol'],
                serializer.validated_data['sys_bp'],
                serializer.validated_data['dia_bp'],
                serializer.validated_data['weight'] / (serializer.validated_data['height']/100)**2,
                serializer.validated_data['heart_rate'],
                serializer.validated_data['glucose']
            ]

            prediction_model = PredictionModel.objects.filter(is_active=True).first()
            result = prediction_model.predict([user_data])
            return Response({"risk": result})
        return Response(serializer.errors)

