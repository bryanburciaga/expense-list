from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'home.html', {'expenses': expenses})

@login_required
def expense_detail(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expense/detail.html', {
        'expense': expense,
    })

def signup(request):
    error_message = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Signup Input invalid - Please try again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error': error_message })

class ExpenseCreate(LoginRequiredMixin, CreateView):
    model = Expense
    fields = ('name', 'description', 'cost')
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ExpenseUpdate(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'

class ExpenseDelete(LoginRequiredMixin, DeleteView):
    model =  Expense
    success_url = '/'