from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Meal


# Create your views here.
def meal_logView(request):
    all_meals = Meal.objects.all()
    return render(request, 'meal_log.html',
                  {'all_items': all_meals})


def addMeal(request):
    form = request.POST
    new_meal = Meal(date=form['date'], time=form['time'], description=form['description'])
    new_meal.save()
    return HttpResponseRedirect('/meallog/')

def deleteMeal(request, todo_id):
    meal_to_delete = Meal.objects.get(id=todo_id)
    meal_to_delete.delete()
    return HttpResponseRedirect('/meallog/')