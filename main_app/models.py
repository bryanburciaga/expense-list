from django.db import models
from django.urls import reverse
# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('expenses_detail', kwargs={'expense_id': self.id})