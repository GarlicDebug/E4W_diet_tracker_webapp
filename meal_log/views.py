from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Meal


# Create your views here.
def meal_logView(request):
    all_meals = Meal.objects.filter(user=request.user)
    return render(request, 'meal_log.html',
                  {'all_items': all_meals})


def addMeal(request):
    form = request.POST
    new_meal = Meal(user=request.user, date=form['date'], time=form['time'],
                    description=form['description'], quantity=form['quantity'])
    new_meal.save()
    return HttpResponseRedirect('/meallog/')


def deleteMeal(request, todo_id):
    meal_to_delete = Meal.objects.get(id=todo_id)
    meal_to_delete.delete()
    return HttpResponseRedirect('/meallog/')
