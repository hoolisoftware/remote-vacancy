from markdown import markdown
from autoslug import AutoSlugField
from datetime import timedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.utils import timezone

from .manager import VacancyActiveManager, VacancyArchivedManager

User = get_user_model()

class VacancyTag(models.Model):
    title = models.CharField('title', max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, primary_key=True)

    class Meta:
        verbose_name = 'vacancy tag'
        verbose_name_plural = 'vacancy tags'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<{self.title}>'

class VacancyPosition(models.Model):
    title = models.CharField('title', max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, primary_key=True)

    class Meta:
        verbose_name = 'vacancy position'
        verbose_name_plural = 'vacancy positions'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<{self.title}>'

class Location(models.Model):
    title = models.CharField('title', max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True, primary_key=True)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f'<{self.title}>'


class Vacancy(models.Model):

    SALARY_TYPES = (
        ('cash','Cash'),
        ('stablecoins','Stablecoins'),
        ('crypto','Crypto'),
        ('your_tokens','Your Tokens'),
        ('nft','NFT'),
    )

    JOB_TYPES = (
        ('fulltime','Full-Time'),
        ('parttime','Part-Time'),
        ('up2u','UP2U'),
        ('temporary','Temporary'),
    )

    company_logo = models.ImageField('company logo', upload_to='vacancies/logo/',default='vacancies/logo/default/default.png')
    publicant = models.ForeignKey(User, to_field='id', verbose_name='publicant', related_name='vacancies', on_delete=models.CASCADE)

    company_name = models.CharField('company name *', max_length=50)
    description = models.TextField('description *')
    to_apply = models.URLField('where to apply (URL) *')
    company_website = models.URLField('company website URL *')
    company_twitter = models.URLField('company twitter URL *')
    communication = models.TextField('data for getting in touch with you *')

    verified = models.BooleanField('company is verified? (admin)', default=False)
    hot = models.BooleanField('vacancy is hot? (payment to admins)', default=False)
    archived = models.BooleanField('vacancy is archived? (payment)', default=False)

    job_type = models.CharField('job type', default='fulltime', max_length=50, choices=JOB_TYPES)
    salary_type = models.CharField('salary type', default='cash', max_length=50, choices=SALARY_TYPES)
    salary = models.CharField('salary amount *', max_length=50)

    position = models.ForeignKey(VacancyPosition, to_field='slug', default='1', verbose_name='position', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, verbose_name='location', to_field='slug', on_delete=models.SET_DEFAULT, default='ww')
    tags = models.ManyToManyField(to=VacancyTag, verbose_name='tags')

    published = models.DateTimeField('publication date', auto_now_add=True)

    objects = models.Manager()
    active = VacancyActiveManager()
    archive = VacancyArchivedManager()

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'

    @property
    def description_html(self):
        return markdown(self.description)

    @property
    def since_published(self):

        _ = seconds= timezone.now().timestamp() - self.published.timestamp()

        i1 = {
            'm': _ // (60*60*25*30),
            'w': _ // (60*60*25*7),
            'd': _ // (60*60*24),
            'h': _ // (60*60),
            'm': _ // (60),
            's': _
        }
        i2 = {
            x: y for x, y in i1.items() if y
        }

        _ = min(zip(i2.values(), i2.keys()))
        return f'{int(_[0])}{_[1]}'

    def __str__(self):
        return f'{self.company_name} - {self.position} ({self.requests.count()})'

    def __repr__(self):
        return f'<{self.company_name} - {self.position} ({self.requests.count()})'


class VacancyRequest(models.Model):
    applicant = models.ForeignKey(User, related_name='requests', to_field='id', default='1', verbose_name='applicant', on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, related_name='requests', to_field='id', default='1', verbose_name='vacancy', on_delete=models.CASCADE)
    description = models.TextField('description')
    cv = models.FileField('CV', upload_to='vacancies/cv/', validators=[FileExtensionValidator(allowed_extensions=['doc','pdf','md'])])

    class Meta:
        verbose_name = 'vacancy request'
        verbose_name_plural = 'vacancy requests'

    def __str__(self):
        return f'{self.applicant} -> {self.vacancy}'

    def __repr__(self):
        return f'<{self.applicant} -> {self.vacancy}>'
