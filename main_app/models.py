from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Totals(models.Model):
    total = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('expenses_detail', kwargs={'expense_id': self.id})