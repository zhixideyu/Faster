from django.db import models
from faker import Faker
from django.contrib.auth.models import AbstractUser

# Create your models here.
fake = Faker()


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='昵称', default='虚拟-{}'.format(fake.name()))
    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True, default='{}'.format(fake.simple_profile()['birthdate']))
    address = models.CharField(max_length=50, verbose_name='住址')
    mobile = models.CharField(max_length=11, verbose_name='手机号', null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m', verbose_name='头像')

    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
