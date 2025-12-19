from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Expense
from datetime import datetime
from django.db.models import Sum

# ---------------- SIGN UP ----------------
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'app1/home.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'app1/home.html')


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'app1/login.html', {'error': 'Invalid credentials'})

    return render(request, 'app1/login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    selected_month = request.GET.get('month')
    expenses = Expense.objects.filter(user=request.user)

    # Filter by month if selected
    month_int = None
    if selected_month:
        try:
            month_int = int(selected_month)
            expenses = expenses.filter(date__month=month_int)
        except ValueError:
            month_int = None

    # ADD EXPENSE
    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')

        if category and amount:
            Expense.objects.create(
                user=request.user,
                category=category,
                amount=float(amount)
            )
        return redirect('dashboard')

    # CALCULATIONS
    category_totals = {}
    monthly_total = 0

    for exp in expenses:
        category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount
        monthly_total += exp.amount

    remaining_balance = 50000 - monthly_total  # Example: fixed budget

    # Monthly totals for bar chart
    monthly_labels = [datetime(2000, m, 1).strftime('%b') for m in range(1, 13)]
    monthly_data = []
    for m in range(1, 13):
        month_total = Expense.objects.filter(user=request.user, date__month=m).aggregate(
            total_amount=Sum('amount')
        )['total_amount'] or 0
        monthly_data.append(month_total)

    context = {
        'expenses': expenses.order_by('-date'),
        'category_totals': category_totals,
        'monthly_total': monthly_total,
        'remaining_balance': remaining_balance,
        'months': range(1, 13),
        'selected_month': month_int,
        'monthly_labels': monthly_labels,
        'monthly_data': monthly_data,
    }

    return render(request, 'app1/dashboard.html', context)


# ---------------- DELETE EXPENSE ----------------
@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('dashboard')


# ---------------- EDIT EXPENSE ----------------
@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)

    if request.method == 'POST':
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        if category and amount:
            expense.category = category
            expense.amount = float(amount)
            expense.save()
        return redirect('dashboard')

    return render(request, 'app1/edit_expense.html', {'expense': expense})
