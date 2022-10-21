from django.db import models
from django.contrib.auth.models import AbstractUser

LIMIT_VACANCIES = 10


class User(AbstractUser):
    ACCOUNT_TYPES = (
        ('employer', 'Employer'),
        ('employee', 'Employee')
    )

    avatar = models.ImageField('avatar', upload_to='users/avatar/', default='users/avatar/default/default.png')
    account_type = models.CharField('account type', max_length=50, choices=ACCOUNT_TYPES, default='employee')
