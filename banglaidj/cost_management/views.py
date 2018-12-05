from django.shortcuts import render
from .models import Expense


# Create your views here.

def my_expense(request):
    expenses = Expense.objects.all()
    print(expenses)
    return render(request, 'cost/my_expense.html', {'expenses': expenses})