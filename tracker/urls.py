from django.urls import path
from .views import expenses_list
from . import views

urlpatterns = [
    path('expenses/', expenses_list),
    path("add-expense/", views.add_expense, name="add_expense"),
    path("expenses/delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
]
