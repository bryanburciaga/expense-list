from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/<int:expense_id>/', views.expense_detail, name='expenses_detail'),
    path('expenses/create/', views.ExpenseCreate.as_view(), name='expenses_create'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expenses_update'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expenses_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]