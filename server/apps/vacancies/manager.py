from django.db import models

class VacancyActiveManager(models.Manager):
    def get_queryset(self):
        return super(VacancyActiveManager,self).get_queryset().filter(archived=False).order_by('-published')

class VacancyArchivedManager(models.Manager):
    def get_queryset(self):
        return super(VacancyArchivedManager).get_queryset().filter(archived=True).order_by('-published')