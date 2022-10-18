from django.shortcuts import render
from .models import Expense


def home(request):
    expenses = Expense.objects.filter()
    return render(request, 'home.html', {'expenses': expenses})

def expense_detail(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expenses/detail.html', {
        'expense': expense,
    })

