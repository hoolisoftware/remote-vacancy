from django.contrib import admin

from . import models

admin.site.register(models.Location)
admin.site.register(models.VacancyTag)
admin.site.register(models.VacancyPosition)

@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'publicant',
        'job_type',
        'salary_type',
        'salary'
    )

@admin.register(models.VacancyRequest)
class VacancyRequestAdmin(admin.ModelAdmin):
    list_display = (
        'applicant',
        'vacancy'
    )