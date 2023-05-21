from django.contrib import admin
from .models import PredictionModel
# Register your models here.

class PredictionModelAdmin(admin.ModelAdmin):
    model = PredictionModel


admin.site.register(PredictionModel, PredictionModelAdmin)