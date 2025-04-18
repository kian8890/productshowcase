from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),  # هذا هو السطر المضاف
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
