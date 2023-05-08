from django.contrib import admin
from .models import PredictionModel
# Register your models here.

class PredictionModelAdmin(admin.ModelAdmin):
    model = PredictionModel

    def has_add_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(PredictionModel, PredictionModelAdmin)