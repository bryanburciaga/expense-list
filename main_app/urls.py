from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('expenses/<int:expense_id>/', views.expense_detail, name='expenses_detail'),
]