from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('account-settings/', views.UserUpdateView.as_view(), name='user-update'),
    path('account-password/', views.UserUpdatePasswordView.as_view(), name='user-update-password'),

    path('logout/', views.LogoutView.as_view(), name='logout')
]