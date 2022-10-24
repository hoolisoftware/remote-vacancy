from rest_framework import serializers

from apps.vacancies.models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    position = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Vacancy
        fields = (
            'id',
            'publicant',
            'company_logo',
            'company_name',
            'description_html',
            'to_apply',
            'company_website',
            'company_twitter',
            'communication',
            'verified',
            'hot',
            'archived',
            'job_type',
            'salary_type',
            'salary',
            'position',
            'location',
            'tags',
            'since_published',
            'published'
        )