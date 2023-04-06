from django import forms


class UserInputForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=1, max_value=100)
    sex = forms.ChoiceField(label='Sex', choices=[('0', 'Female'), ('1', 'Male')], widget=forms.RadioSelect)
    current_smoker = forms.BooleanField(label='Current Smoker', required=False)
    cigs_per_day = forms.IntegerField(label='Cigarettes per day', min_value=0, max_value=50)
    bp_meds = forms.BooleanField(label='On Blood Pressure Medication', required=False)
    prevalent_stroke = forms.BooleanField(label='History of Stroke', required=False)
    prevalent_hyp = forms.BooleanField(label='Hypertension', required=False)
    diabetes = forms.BooleanField(label='Diabetes', required=False)
    tot_chol = forms.IntegerField(label='Total Cholesterol', min_value=100, max_value=400)
    sys_bp = forms.FloatField(label='Systolic Blood Pressure', min_value=70, max_value=250)
    dia_bp = forms.FloatField(label='Diastolic Blood Pressure', min_value=40, max_value=150)
    bmi = forms.FloatField(label='Body Mass Index (BMI)', min_value=15, max_value=60)
    heart_rate = forms.IntegerField(label='Heart Rate', min_value=40, max_value=150)
    glucose = forms.IntegerField(label='Glucose', min_value=40, max_value=500)
