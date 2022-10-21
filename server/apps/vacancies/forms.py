from core.mixins import AddClassNameMixin, AddAttributeMixin
from django.forms import ModelForm

from . import models

class VacancyForm(AddClassNameMixin, AddAttributeMixin, ModelForm):

    not_modify_fields = ['tags']
    custom_attributes = {
        'company_logo': {
            'onchange': 'document.getElementById("companyLogo").src = window.URL.createObjectURL(this.files[0])',
        },
        'to_apply': {
            'rows': '1'
        },
        'description': {
            'rows': '3'
        },
        'communication': {
            'rows': '3'
        },
        'tags': {
            'id': 'slim-select',
            'class': ''
        }
    }
    
    class Meta:
        model = models.Vacancy
        fields = [
            'company_logo',
            'company_name',
            'to_apply',
            'description',
            'company_website',
            'company_twitter',
            'job_type',
            'position',
            'salary_type',
            'salary',
            'location',
            'tags',
            'communication',
        ]
        help_texts = {
            'company_name': "Your company's brand/trade name: without Inc., Ltd., B.V., Pte., etc.",
            'position': 'Please specify as single job position like "Marketing Manager" or "Node JS Developer", not a sentence like "Looking for PM / Biz Dev / Manager". We know your job is important but please DO NOT WRITE IN FULL CAPS. If posting multiple roles, please create multiple job posts. A job post is limited to a single job. We only allow real jobs, absolutely no MLM-type courses "learn how to work online" please.',
            'to_apply': 'Link to applying page, phone number etc',
            'tags': "Short tags are preferred. Use tags like industry and tech stack. The first 3 or 4 tags are shown on the site, the other tags aren't but the job will be shown on each tag specific page (like /remote-react-jobs). We also sometimes generate tags automatically after you post/edit to supplement.",
            'location': 'If you\'d only like to hire people from a specific location or timezone this remote job is restricted to.',
        }

