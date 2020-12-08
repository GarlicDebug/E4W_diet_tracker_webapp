from django.forms import ModelForm
from meal_log.models import Meal

class MealModelForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['date', 'time', 'description']
        labels = {'date': 'Meal Date', 'time': 'Meal Time', 'description': 'Meal Description'}