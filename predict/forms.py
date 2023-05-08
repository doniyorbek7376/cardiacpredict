from django import forms


class UserInputForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=1, max_value=100, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    sex = forms.ChoiceField(label='Sex', choices=[('0', 'Female'), ('1', 'Male')], widget=forms.RadioSelect(attrs={
        'class': 'radio-inline',
    }))
    cigs_per_day = forms.IntegerField(label='Cigarettes per day', min_value=0, max_value=50, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    bp_meds = forms.BooleanField(label='On Blood Pressure Medication', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    prevalent_stroke = forms.BooleanField(label='History of Stroke', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    prevalent_hyp = forms.BooleanField(label='Hypertension', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    diabetes = forms.BooleanField(label='Diabetes', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'
    }))
    tot_chol = forms.IntegerField(label='Total Cholesterol', min_value=100, max_value=400, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    sys_bp = forms.FloatField(label='Systolic Blood Pressure', min_value=70, max_value=250, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    dia_bp = forms.FloatField(label='Diastolic Blood Pressure', min_value=40, max_value=150, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    weight = forms.FloatField(label='Weight (kg)', min_value=0, max_value=200, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    height = forms.IntegerField(label='Height (cm)', min_value=0, max_value=300, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    heart_rate = forms.IntegerField(label='Heart Rate', min_value=40, max_value=150, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    glucose = forms.IntegerField(label='Glucose', min_value=40, max_value=500, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
