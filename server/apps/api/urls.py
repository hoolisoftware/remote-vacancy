from django.urls import path

from . import views

urlpatterns = [
    path('vacancy-archive-toggle/<int:id>/', views.VacancyArchiveToggleAPIView.as_view(), name='vacancy-arhcive-toggle'),
    path('vacancy-delete/<int:id>/', views.VacancyDeleteAPIView.as_view(), name='vacancy-delete'),
    path('vacancy-list/', views.VacancyListAPIView.as_view(), name='vacancy-list'),
]