from django.urls import path

from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),

    path('vacancy-list/', views.VacancyListView.as_view(), name='vacancy-list'),
    path('vacancy-list-archive/', views.VacancyListArchiveView.as_view(), name='vacancy-list-archive'),
    path('vacancy-create/', views.VacancyCreateView.as_view(), name='vacancy-create'),
    path('vacancy-update/<int:pk>', views.VacancyUpdateView.as_view(), name='vacancy-update'),
    path('vacancy-payment/<int:pk>', views.VacancyPaymentView.as_view(), name='vacancy-payment'),
    path('vacancy/<int:pk>', views.VacancyDetailView.as_view(), name='vacancy-detail'),

    path('vacancy-request-create/', views.VacancyRequestCreateView.as_view(), name='vacancy-request-create'),
    path('vacancy-request-list/<int:pk>', views.VacancyRequestListView.as_view(), name='vacancy-request-list'),

]