from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=255)
    date_of_expense = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # powiązanie z kategorią (dropdown w adminie i formularzach)
    category_of_expense = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='expenses'
    )

    def __str__(self):
        return f"{self.name} - {self.amount} zł ({self.category_of_expense})"


