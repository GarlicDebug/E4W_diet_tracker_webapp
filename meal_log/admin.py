from django.contrib import admin

# Register your models here.
from meal_log.models import Meal

class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'description', 'quantity', 'nutrition')

admin.site.register(Meal, MealAdmin)