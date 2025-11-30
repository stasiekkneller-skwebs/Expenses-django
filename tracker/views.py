from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExpenseForm
from .models import Category, Expense

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/expenses/")   # lub inna strona po zapisie
    else:
        form = ExpenseForm()

    return render(request, "add_expense.html", {"form": form})

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect("/expenses/")




def expenses_list(request):
    selected_category = request.GET.get("category")  # pobierz wybraną kategorię z URL-a
    categories = Category.objects.all()

    if selected_category and selected_category != "all":
        expenses = Expense.objects.filter(category_of_expense_id=selected_category)
    else:
        expenses = Expense.objects.all()

    context = {
        "expenses_list": expenses,
        "categories": categories,
        "selected_category": selected_category,
    }
    return render(request, "expenses_list.html", context)