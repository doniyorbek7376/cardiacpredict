from django.db import models
import pickle

class PredictionModel(models.Model):
    name = models.CharField(max_length=200)
    model_file = models.FileField(upload_to='models/')
    accuracy = models.FloatField()

    def predict(self, user_data):
        # Load the trained model from disk
        with self.model_file.open(mode='rb') as f:
            model = pickle.load(f)

        # Use the model to predict the user's risk of cardiac disease
        prediction = model.predict_proba(user_data)[:, 1]
        return prediction

    def __str__(self):
        return "PredictionModel"