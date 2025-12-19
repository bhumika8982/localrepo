from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-expense/<int:id>/', views.delete_expense, name='delete_expense'),
    path('edit-expense/<int:id>/', views.edit_expense, name='edit_expense'),

]
