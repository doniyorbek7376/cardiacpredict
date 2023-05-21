from django.db import models
import pickle


class PredictionModel(models.Model):
    name = models.CharField(max_length=200)
    model_file = models.FileField(upload_to='models/')
    accuracy = models.FloatField()
    is_active = models.BooleanField(default=False)

    def predict(self, user_data):
        # Load the trained model from disk
        with self.model_file.open(mode='rb') as f:
            model = pickle.load(f)

        # Use the model to predict the user's risk of cardiac disease
        prediction = model.predict_proba(user_data)[:, 1]
        return prediction

    def __str__(self):
        return f"PredictionModel {self.name}"


class PredictionRequest(models.Model):
    age = models.IntegerField()
    sex = models.BooleanField()
    cigs_per_day = models.IntegerField()
    bp_meds = models.BooleanField()
    prevalent_stroke = models.BooleanField()
    prevalent_hyp = models.BooleanField()
    diabetes = models.BooleanField()
    tot_chol = models.IntegerField()
    sys_bp = models.IntegerField()
    dia_bp = models.IntegerField()
    weight = models.FloatField()
    height = models.IntegerField()
    heart_rate = models.IntegerField()
    glucose = models.IntegerField()
