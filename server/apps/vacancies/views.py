from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from . import forms
from . import models

class HomeView(generic.ListView):
    model = models.Vacancy
    template_name = 'vacancies/home.django-html'

    def get_queryset(self):
        return models.Vacancy.active.all()


class AboutView(generic.TemplateView):
    template_name = 'vacancies/about.django-html'

class PrivacyPolicyView(generic.TemplateView):
    template_name = 'vacancies/privacy-policy.django-html'

class TermsOfServiceView(generic.TemplateView):
    template_name = 'vacancies/terms-of-service.django-html'


class VacancyRequestCreateView(generic.CreateView):
    model = models.VacancyRequest
    fields = (
        'description',
        'cv'
    )
    template_name = 'vacancies/vacancy-request-create.django-html'


class VacancyRequestListView(LoginRequiredMixin,generic.ListView):
    model = models.VacancyRequest
    template_name = 'vacancies/vacancy-request-list.django-html'

    def get_queryset(self):
        return get_object_or_404(models.Vacancy, pk=self.kwargs["pk"]).requests.all()   


class VacancyListView(LoginRequiredMixin,generic.ListView):
    model = models.Vacancy
    template_name = 'vacancies/vacancy-list.django-html'

    def get_queryset(self):
        return self.request.user.vacancies.all().filter(archived=False).order_by('-published')


class VacancyListArchiveView(LoginRequiredMixin, generic.ListView):
    model = models.Vacancy
    template_name = 'vacancies/vacancy-list-archive.django-html'
    
    def get_queryset(self):
        return self.request.user.vacancies.all().filter(archived=True).order_by('-published')


class VacancyPaymentView(generic.DetailView):
    model = models.Vacancy
    template_name = 'vacancies/vacancy-payment.django-html'


class VacancyCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Vacancy
    form_class = forms.VacancyForm
    template_name = 'vacancies/vacancy-create-update.django-html'
    success_url = reverse_lazy('vacancies:vacancy-list')

    def form_valid(self, form):
        form.instance.publicant = self.request.user
        messages.success(self.request, 'Vacancy has been created! And, thank you...')
        return super().form_valid(form)


class VacancyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Vacancy
    form_class = forms.VacancyForm
    template_name = 'vacancies/vacancy-create-update.django-html'


class VacancyDetailView(generic.DetailView):
    model = models.Vacancy
    template_name = 'vacancies/vacancy-detail.django-html'


