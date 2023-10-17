import helper
import logging
from matplotlib import pyplot as plt

def calculate_total_expenses(user_history):
    total_expenses = {}
    for record in user_history:
        date, category, amount = record.split(",")
        amount = float(amount)
        if category not in total_expenses:
            total_expenses[category] = amount
        else:
            total_expenses[category] += amount
    return total_expenses

def is_overall_budget_exceeded(user_history, overall_budget):
    total_expenses = calculate_total_expenses(user_history)
    total_spent = sum(total_expenses.values())
    
    if overall_budget is not None:
        if total_spent > overall_budget:
            return True
    return False

def calculate_expenses_by_category(user_history):
    expenses_by_category = {}
    for record in user_history:
        _, category, amount = record.split(",")
        amount = float(amount)
        if category not in expenses_by_category:
            expenses_by_category[category] = amount
        else:
            expenses_by_category[category] += amount
    return expenses_by_category

def display_pie_chart(user_history, user_budget):
    expenses_by_category = calculate_expenses_by_category(user_history)
    categories = expenses_by_category.keys()
    expenses = expenses_by_category.values()
    dates = []
    
    # Extract the dates for each category
    for category in categories:
        dates_str = [record.split(',')[0] for record in user_history if category in record]
        dates.append(dates_str)

    fig, ax1 = plt.subplots(2, 1, figsize=(8, 8))
    
    return fig